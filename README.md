# Marten Numpad

Marten 22 is a wireless, 21/22 key numpad named after a [cute, woodland animal](https://en.wikipedia.org/wiki/American_marten). (There is no meaning to the name other than that I like them, and I couldn't find any existing keyboards named after them.) It is based on the nRF52840 SoC and uses a 3D printed case.

It has the following features:

- USB and Bluetooth support with [ZMK Firmware](https://zmk.dev/)
- Hot swap sockets for MX switches
- Supports Li-Ion or LiPo batteries up to 68x40x8 mm or 55x44x8 mm.
- The top-left and top-right keys can be replaced with encoders.
  - Supports [SKYLOONG keyboard knobs](https://skyloongtech.com/skyloong-keyboard-knobs/) (silicone/ABS cover versions only) or a separate encoder PCB with 3D printed case
- Any pair of two keys on the top row can be replaced with a display.
  - This uses a separate display PCB and connects with a ribbon cable.
  - nice!view and SSD1306 OLED display modules are supported.

A 22/23 key layout with a split plus key would be possible, but it would require a separate PCB from the 21/22 key layout. There is no way to fit three hot swap sockets into the space for the plus key without rotating the 1U keys 90 degrees, and this could damage keycaps, so I opted not to include that as an option.

(TODO: add renders/pictures of the completed keyboard)

> ⚠️ WARNING ⚠️ </br>
> I have received PCBs but they have not been fully tested. You should probably not make one yourself until I verify that everything works.

**Hardware status:**

| Component                | Status   |
| ------------------------ | -------- |
| Numpad PCB               | Untested |
| nice!view display module | Untested |
| OLED display module      | Untested |
| Encoder module           | Untested |
| 3D printed case          | Untested |

**Firmware status:**

| Component             | Status          |
| --------------------- | --------------- |
| Base firmware         | Not implemented |
| Numlock LED           | Not implemented |
| Custom display screen | Not implemented |
| nPM1300 charger       | Not implemented |
| nPM1300 fuel gauge    | Not implemented |
| Power button          | Not implemented |

## PCB

KiCad files for the PCBs can be found in the [pcb](./pcb) directory. There are a few PCBs:

- [numpad.kicad_pro](./pcb/numpad.kicad_pro) is the main PCB.
- [display.kicad_pro](./pcb/display.kicad_pro) is an optional daughterboard for connecting a [nice!view](https://nicekeyboards.com/nice-view/) display.
- [display_oled.kicad_pro](./pcb/display_oled.kicad_pro) is an optional daughterboard for connect an SSD1306 OLED display.
  - It works with the common SSD1306 display modules you can find from a wide variety of sellers, but make sure to get one which does _not_ have a pin header already soldered.
- [encoder.kicad_pro](./pcb/encoder.kicad_pro) is an optional daughterboard for an EC11 encoder.
- [peripheral.kicad_pro](./pcb/peripheral.kicad_pro) is template for creating your own daughterboards.

The main PCB requires a couple of parts which are not hand solderable, so PCB assembly is required.

The display and encoder PCBs are hand solderable (though the SMD parts on the encoder are difficult to solder). The encoder PCB also requires modifying the EC11 encoder by clipping its pins short.

Instructions for ordering and assembling the hardware can be found on the wiki.

(TODO: add a wiki page)

[PCBWay](https://www.pcbway.com/) provided me a discount on PCB assembly in exchange for sharing pictures of the completed board and talking about my experience ordering from them. I will add details to the wiki for this once I've finished testing the hardware.

(TODO: add a wiki page)

### Custom Peripherals

The numpad PCB has a [Molex 5051100692](https://www.molex.com/en-us/products/part-detail/5051100692) FFC connector (labeled "Display") which can be used to connect to a daughterboard using a 6-pin ribbon cable. It provides 3.3 V power, two ground pins, and three GPIO pins. While its main purpose is to connect a display, you can use this to add your own custom hardware as well.

(TODO: add a wiki page explaining custom hardware and firmware)

## Case

TODO

## Firmware

TODO

## Credits

- Fonts:
  - [Fredoka](https://fonts.google.com/specimen/Fredoka)
- Libraries:
  - [marbastlib](https://github.com/ebastler/marbastlib)
  - Some footprints are modified from the [KiCad Libraries](https://gitlab.com/kicad/libraries/kicad-footprints)
- 3D models
  - Some 3D models are generated using [KiCad Packages3D Generator](https://gitlab.com/kicad/libraries/kicad-packages3D-generator)
  - [128x32 OLED display](https://grabcad.com/library/0-91-128x32-oled-display-1)
  - [JST SH connector](https://grabcad.com/library/jst-sh-smd-connectors-1)
  - Models for the following parts are provided by their respective manufacturers:
    - [Bourns PEC11L](https://www.bourns.com/products/encoders/contacting-encoders/product/PEC11L)
    - [HRO TYPE-C-31-M-12](https://www.snapeda.com/parts/TYPE-C-31-M-12/HRO%20Electronics%20Co.,%20Ltd./view-part/)
    - [Kingbright APTR3216-VFX](https://www.kingbrightusa.com/product.asp?catalog_name=LED&product_id=APTR3216-VFX)
    - [Molex 781710002](https://www.molex.com/en-us/products/part-detail/781710002)
    - [Molex 5051100692](https://www.molex.com/en-us/products/part-detail/5051100692)
    - [Mill-Max 811-22-002-30-004101](https://www.mill-max.com/products/spring-loaded/pogo-pin-header-strip/811/30-004101/811-22-002-30-004101)
    - [Mill-Max 811-22-004-30-001101](https://www.mill-max.com/products/spring-loaded/pogo-pin-header-strip/811/30-001101/811-22-004-30-001101)
    - [Mill-Max 821-22-005-10-001101](https://www.mill-max.com/products/spring-loaded/pogo-pin-header-strip/821/10-001101/821-22-005-10-001101)
    - [Raytac MDBT50Q-1MV2](https://www.raytac.com/product/ins.php?index_id=24)
    - [Würth 9774005243R](https://www.we-online.com/en/components/products/SMSI_SMT_STEEL_SPACER_M2_THREAD_INTERNAL)
