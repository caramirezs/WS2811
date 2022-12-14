import time
import board
import neopixel
import re
import math

n_strips = 1
N_PIXEL = 50 * n_strips
PIXEL_PIN = board.D18
BRIGHTNESS=0.2
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(PIXEL_PIN, N_PIXEL, auto_write=False,
                           brightness=BRIGHTNESS, pixel_order=ORDER)

pixels[9] =(255, 255, 255)
pixels.show()
