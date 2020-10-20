import base64

from PIL import Image
import os, sys

ip = 'http://66.97.46.179'
port = 3003
s = socket.socket()
s.connect((ip, port))

image_path = '/home/pi/Desktop/test-client-cam/snapshot.png'

if image_path != '':
    with open(image_path, "rb") as imageFile:
        image_data = base64.b64encode(imageFile.read())
else:
    image_data = 'ERROR'


s.send(image_data)

s.close()