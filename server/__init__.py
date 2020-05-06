import socket

from server.server import Server


# IP and PORT of the server
IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
# Header length in bytes
HEADER_LENGTH = 2
# String encoding format
FORMAT = 'UTF-8'

server = Server(IP, PORT, HEADER_LENGTH, FORMAT)
