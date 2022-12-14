# Based on code from https://github.com/standupmaths/xmastree2020

import board
import neopixel
import time 
import sys

NUMBEROFLEDS = 255
pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS,
brightness=0.1) 
ids =  sys.argv[1:]

intervalo = range(int(ids[0]), int(ids[1]))

for id in intervalo:
    i = int(id)
    pixels[i] = (255,255,255)
    time.sleep(1)
    pixels[i] = (0, 0, 0)
print("Done")

