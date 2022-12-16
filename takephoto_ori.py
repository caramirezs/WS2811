import cv2

cam = cv2.VideoCapture('http://192.168.1.136:4747/mjpegfeed?640x480')

while True:
	ret, image = cam.read()
	cv2.imshow('Imagetest',image)
	k = cv2.waitKey(1)
	if k != -1:
		break
cv2.imwrite(f'./img/IMG_ori_y2.jpg', image)
cam.release()
cv2.destroyAllWindows()
