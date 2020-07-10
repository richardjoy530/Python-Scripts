from ppadb.client import Client
import cv2
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]
while True:
    image = device.screencap()

    with open('screen.png', 'wb') as f:
        f.write(image)
    image = cv2.imread('screen.png',0)
    image = numpy.array(image, dtype=numpy.uint8)
    cv2.imshow('test',image)
    key = cv2.waitKey(5)
    if key == 'q':
        break

cv2.waitKey(0)
cv2.destroyAllWindows()


