import socket
import threading


class Server:

    def __init__(self, IP, PORT, HEADER_LENGTH, FORMAT):
        self.ADDR = (IP, PORT)
        self.HEADER_LENGTH = HEADER_LENGTH
        self.FORMAT = FORMAT

        self.connected = False

        # Initialize the server socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.ADDR)

    def handle_client(self, conn, addr):
        print(f'[NEW CONNECTION] Client connected from {addr}')

        while True:
            with conn:
                msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
                if not msg_length:
                    break
                msg = conn.recv(msg_length).decode(self.FORMAT)
                conn.send('Msg received'.encode(self.FORMAT))

        conn.close()

    def listen(self):
        """
        Listen for incoming connections.
        """
        self.socket.listen()
        print(f'[LISTENING] Server is listening on {self.ADDR}')

        while True:
            conn, addr = self.socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

    def start(self):
        """
        Start the server.
        """
        print('[STARTING] Server is starting...')

        self.listen()
