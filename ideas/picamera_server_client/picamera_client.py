import io
import time
# import picamera
import socket
import cv2
host = '127.0.0.1'
port = 5001
sock = socket.socket()
print('connecting...')
sock.connect((host, port))
"""
# Create an in-memory stream
my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture(my_stream, 'jpeg')
"""
port = 0
video_capture = cv2.VideoCapture(port)
return_value, image = video_capture.read()
cv2.imwrite('send_file.jpg', image)
with open('send_file.jpg','rb') as file: # may be needed
    print('Sending...')
    l = file.read(1024)
    while l:
        print('Sending...')
        sock.send(l)
        l = file.read(1024)
    print('done sending.')
sock.close()
