import socket

class ConnectionHandler:
    """class handling connection"""

    def __init__(self, port):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        pass

    def receive(self):
        pass

if __name__ == "__main__":

    connection = ConnectionHandler(8090)



