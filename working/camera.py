import picamera
from time import sleep

camera = picamera.PiCamera()
print('taking photo...')
camera.capture('image.jpg')

print('showing preview for 60 seconds...')
camera.start_preview()
sleep(60)
camera.stop_preview()

print('recording 30 seconds of footage...')
camera.start_recording('test.h264')
sleep(30)
camera.stop_recording()

print('test finished')
