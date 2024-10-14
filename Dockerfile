# syntax=docker/dockerfile:1
FROM ghcr.io/inti-cmnb/kicad8_auto_full:latest

RUN apt update \
    && apt install -y unzip wget \
    && rm -rf /var/lib/apt/lists/*

# Add fonts
COPY fonts/*.ttf /usr/share/fonts/truetype/fredoka/
RUN fc-cache

# Add marbastlib 3D models
ARG models_dir8=/root/.local/share/kicad/8.0/3rdparty/3dmodels
ARG models_dir7=/root/.local/share/kicad/7.0/3rdparty/3dmodels
ARG models_dir6=/root/.local/share/kicad/6.0/3rdparty/3dmodels

RUN wget https://github.com/ebastler/marbastlib/releases/download/2024.08.18/KiCAD-PCM-2024.08.18.zip -O ~/marbastlib.zip \
    && unzip ~/marbastlib.zip -d ~/marbastlib \
    && rm ~/marbastlib.zip \
    && mkdir -p ${models_dir8}/com_github_ebastler_marbastlib \
    && cp ~/marbastlib/3dmodels/* ${models_dir8}/com_github_ebastler_marbastlib \
    && rm -rf ~/marbastlib \
    # Symlink KiCad 8 3D models into directories for older versions, because marbastlib
    # has some footprints still referencing KICAD6_3DMODEL_DIR and KICAD7_3DMODEL_DIR.
    && mkdir -p ${models_dir7} \
    && ln -s ${models_dir8}/com_github_ebastler_marbastlib ${models_dir7}/com_github_ebastler_marbastlib \
    && mkdir -p ${models_dir6} \
    && ln -s ${models_dir8}/com_github_ebastler_marbastlib ${models_dir6}/com_github_ebastler_marbastlib

