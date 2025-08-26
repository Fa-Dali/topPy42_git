import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=48084):
        self.host = host
        self.port = port
        self.clients = {}  # Словарь для хранения подключённых клиентов
        self.lock = threading.Lock()  # Блокировка для безопасного обращения к данным

    def handle_client(self, client_socket, address):
        """
        Поток-обработчик для одного клиента.
        """
        try:
            username = client_socket.recv(1024).decode().strip()
            print(f"[+] Новый клиент {address}, Имя: {username}")

            # Регистрация клиента
            with self.lock:
                self.clients[username] = client_socket
                self.broadcast(f"{username} вошёл в чат!\n")

            while True:
                # Получаем сообщение от клиента
                message = client_socket.recv(1024).decode().strip()
                if not message or message.lower() == "exit":
                    break
                elif message.startswith('/'):
                    # Командные последовательности
                    if message == '/exit':
                        break
                else:
                    self.broadcast(f"{username}: {message}\n")
        except Exception as e:
            print(f"Ошибка при работе с клиентом {username}: {e}")
        finally:
            # Удаляем клиента при выходе
            with self.lock:
                del self.clients[username]
                self.broadcast(f"{username} покинул чат.\n")
            client_socket.close()

    def broadcast(self, message):
        """
        Распространяет сообщение всем подключенным клиентам.
        """
        with self.lock:
            for user, sock in list(self.clients.items()):
                try:
                    sock.sendall(message.encode())
                except Exception as e:
                    print(f"Ошибка рассылки сообщения пользователю {user}: {e}")

    def start(self):
        """
        Основной цикл сервера.
        """
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        print(f"Сервер запущен на {self.host}:{self.port}")

        try:
            while True:
                client_socket, address = server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                thread.daemon = True
                thread.start()
        finally:
            server_socket.close()

if __name__ == '__main__':
    server = ChatServer()
    server.start()