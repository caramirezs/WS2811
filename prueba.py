import time
import board
import neopixel
import re
import math

n_strips = 1
N_PIXEL = 50 * n_strips
# PIXEL_PIN = board.D18
# BRIGHTNESS=0.5
# ORDER = neopixel.RGB
#
# pixels = neopixel.NeoPixel(PIXEL_PIN, N_PIXEL, auto_write=False,
#                            brightness=BRIGHTNESS, pixel_order=ORDER)
#
# pixels.fill((0, 255, 0))
pixels = neopixel.NeoPixel(board.D18, N_PIXEL)
pixels.fill((255, 0, 0))