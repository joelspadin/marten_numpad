#!/usr/bin/env python3

"""
Run a command in the kibot Docker container.

Usage:
Run kibot on all PCBs:      ./kibot.py
Run kibot on given PCB:     ./kibot.py numpad
Rebuild Docker image:       ./kibot.py --rebuild
Run a command in Docker:    ./kibot.py -c kibot --help
"""

from contextlib import contextmanager
import shlex
import sys
from pathlib import Path
from subprocess import DEVNULL, CalledProcessError, call, check_call
from typing import Iterable

IMAGE_NAME = "kibot"
PROJECT_DIR = "/usr/src/project"
REPO_DIR = Path(__file__).parent


def build_image():
    check_call(["docker", "build", ".", "-t", IMAGE_NAME])


def kibot_image_valid():
    try:
        check_call(["docker", "image", "inspect", IMAGE_NAME], stdout=DEVNULL)
        return True
    except CalledProcessError:
        return False


def docker_call(args: Iterable[str]):
    if not kibot_image_valid():
        build_image()

    return call(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{REPO_DIR}:{PROJECT_DIR}",
            "-w",
            PROJECT_DIR,
            IMAGE_NAME,
            "bash",
            "-c",
            shlex.join(args),
        ]
    )


@contextmanager
def cleanup():
    try:
        yield
    finally:
        for tempfile in REPO_DIR.rglob("kibot_*.kicad_*"):
            tempfile.unlink()


def parse_args():
    if len(sys.argv) > 1 and sys.argv[1] in ("-c", "--rebuild"):
        return sys.argv[1], sys.argv[2:]

    return None, sys.argv[1:]


def main():
    command, args = parse_args()

    if command == "--rebuild":
        build_image()
        return

    with cleanup():
        if command == "-c":
            retcode = docker_call(args)
        else:
            retcode = docker_call(["./kibot"] + args)

    sys.exit(retcode)


if __name__ == "__main__":
    main()
