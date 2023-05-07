# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio
import digitalio
from adafruit_max7219 import matrices


# You may need to change the chip select pin depending on your wiring
spi = busio.SPI(board.GP2, board.GP3)
cs = digitalio.DigitalInOut(board.GP5)

matrix = matrices.CustomMatrix(spi, cs, 8*4, 8)
matrix.brightness(1)
while True:
    # snake across panel
    for y in range(8):
        for x in range(32):
            if not y % 2:
                matrix.pixel(x, y, 1)
            else:
                matrix.pixel(31 - x, y, 1)
            matrix.show()
            time.sleep(0.05)

    cool_display = "Mikes coola meddelande"
    # scroll a string across the display
    for pixel_position in range(len(cool_display) * 8):
        matrix.fill(0)
        matrix.text(cool_display, -pixel_position, 0)
        matrix.show()
        time.sleep(0.25)
