# Based on code from https://github.com/standupmaths/xmastree2020

import board
import neopixel
import time 
import sys
import cv2

NUMBEROFLEDS = 255
pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS,
brightness=0.1) 
ids =  sys.argv[1:]

intervalo = range(int(ids[0]), int(ids[1]))

cam = cv2.VideoCapture('http://192.168.1.136:4747/mjpegfeed')
time.sleep(5)
ret, image = cam.read()
cv2.imshow('Imagetest',image)


for id in intervalo:
    i = int(id)
    pixels[i] = (255,255,255)
    time.sleep(0.2)
    cv2.imwrite(f'./img/test{i}.jpg', image)
    time.sleep(0.5)
    pixels[i] = (0, 0, 0)
print("Done")

