import socket
import threading
import queue

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 48084

def receive_messages(client_socket, message_queue):
    """
    Функция-приемник сообщений от сервера.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            message_queue.put(message)
        except Exception as e:
            print(f"Ошибка при приеме сообщения: {e}")
            break
    client_socket.close()

def connect_and_join_chat(name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    client_socket.send(name.encode())
    return client_socket

def chat_interface(client_socket):
    """
    Интерфейс чата с двумя нитями: одна для приема сообщений, вторая для отправки.
    """
    message_queue = queue.Queue()
    receiver_thread = threading.Thread(target=receive_messages, args=(client_socket, message_queue))
    receiver_thread.daemon = True
    receiver_thread.start()

    print("Вы вошли в чат. Начинайте общение.")

    while True:
        # Сначала выводим накопившиеся сообщения
        while not message_queue.empty():
            received_message = message_queue.get()
            print(received_message, end='', flush=True)

        # Теперь получаем сообщение от пользователя
        outgoing_message = input()
        if outgoing_message.lower() == "exit":
            client_socket.send("/exit".encode())
            break
        client_socket.send(outgoing_message.encode())

def main():
    username = input("Введите ваше имя: ").strip()
    client_socket = connect_and_join_chat(username)
    chat_interface(client_socket)

if __name__ == '__main__':
    main()