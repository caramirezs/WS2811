# Based on code from https://github.com/standupmaths/xmastree2020

import board
import neopixel
import time 
import sys
import cv2

NUMBEROFLEDS = 250
pixels = neopixel.NeoPixel(board.D18, NUMBEROFLEDS,
brightness=0.1) 
ids =  sys.argv[1:]
intervalo = range(int(ids[0]), int(ids[1]))
run = True      

for id in intervalo:
    i = int(id)
    print(f'LED {i+1} de {NUMBEROFLEDS} -------')
    pixels[i] = (255,255,255)   
    print(f' >> LED:ON')
    cam = cv2.VideoCapture('http://192.168.1.136:4747/mjpegfeed?640x480')
    ret, image = cam.read() # Capture frame-by-frame 
    cv2.imshow('Imagetest',image)
    cv2.waitKey(500)
    cv2.imwrite(f'./img/IMG{i:0>3}_x2.jpg', image)
    print(' >> Imagen guardada')
    pixels[i] = (0, 0, 0)
    print(f' >> LED:OFF\nFIN -------')    
    cam.release()
    cv2.destroyAllWindows()
    time.sleep(2)
    
print("Done")



