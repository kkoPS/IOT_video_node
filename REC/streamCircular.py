import socket
import time
import picamera
import random
import threading

storeVideo = True

def circularVideo():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.rotation = 180
    camera.framerate = 24
    # for the circular buffer local recording
    stream = picamera.PiCameraCircularIO(camera, seconds=20)
    # recording buffer circular continuousl
    camera.start_recording(stream, format='h264')

    while True:
        camera.wait_recording(1)
        if storeVideo:
            # Keep recording for 10 seconds and only then write the
            # stream to disk
            camera.wait_recording(10)
            stream.copy_to('motion.h264')

t1 = threading.Thread(target=circularVideo)
t1.start()
t1.join()



