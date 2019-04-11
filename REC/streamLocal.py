import socket
import time
import picamera
import threading

stopStream = False

def streamVideo():
    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.rotation = 180
            camera.framerate = 24

            server_socket = socket.socket()
            server_socket.bind(('0.0.0.0', 8034))
            server_socket.listen(0)
            connection = server_socket.accept()[0].makefile('wb')
            
            time.sleep(2)
            # Start recording, sending the output to the connection for 60
            # seconds, then stop
            camera.start_recording(connection, format='h264')
            while(True):
                print("streammmm"   )
                if(stopStream):
                    camera.stop_recording()
    finally:
        connection.close()
        client_socket.close()

t1 = threading.Thread(target=streamVideo)
t1.start()
t1.join()
