import socket
import threading

clients = {}

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.username = ""
        clients[self.client_socket] = self
        print(f"Новый участник присоединился: {client_address}")

    def broadcast_message(self, sender_username, message):
        for sock, client in clients.items():
            if sock != self.client_socket:
                sock.sendall(f"[{sender_username}] {message}".encode('utf-8'))  # Отправляем сообщения в utf-8

    def run(self):
        # Первым делом просим клиента ввести имя
        self.client_socket.sendall("Введите ваше имя:".encode('utf-8'))  # Правильно кодируем сообщение в utf-8
        username_bytes = self.client_socket.recv(2048)
        self.username = username_bytes.decode().strip()
        print(f"Участник зарегистрировался под именем: {self.username}")

        while True:
            try:
                data = self.client_socket.recv(2048)
                if not data or data.decode().lower() == 'quit':
                    break
                message = data.decode()
                print(f"Сообщение от [{self.username}]: {message}")
                self.broadcast_message(self.username, message)
            except ConnectionResetError:
                break
        del clients[self.client_socket]
        print(f"Участник покинул чат: {self.username}")
        self.client_socket.close()

# LOCALHOST = "192.168.1.169"
SERVER = "77.220.51.194"
PORT = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server.bind((LOCALHOST, PORT))
server.bind((SERVER, PORT))

print("Сервер запущен и ждёт подключения клиентов...")

while True:
    server.listen(1)
    client_sock, client_addr = server.accept()
    new_client = ClientThread(client_sock, client_addr)
    new_client.start()