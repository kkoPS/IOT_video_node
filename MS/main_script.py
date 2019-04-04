from camera import Camera
from client import Client

camera = Camera()
camera.start()

client = Client(camera)
client.start()