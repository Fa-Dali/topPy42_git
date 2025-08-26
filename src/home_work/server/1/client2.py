import socket

# Настройка адреса сервера
SERVER_IP = "192.168.1.169"
SERVER_PORT = 48084

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect((SERVER_IP, SERVER_PORT))

print("Подключились к серверу!")

try:
    while True:
        # Пользователь вводит сообщение
        user_input = input("Напишите сообщение серверу (для выхода введите 'quit'): ").strip()

        # Если введена команда 'quit'
        if user_input.lower() == "quit":
            break

        # Отправляем сообщение серверу
        client_socket.send(user_input.encode())

        # Получаем ответ от сервера
        reply = client_socket.recv(1024).decode()
        print(f"\nОтвет сервера:\n{reply}\n")

finally:
    client_socket.close()
    print("\nЗавершаем работу клиента.")
