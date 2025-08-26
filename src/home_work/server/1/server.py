import socket

# Настройки сервера
SERVER_IP = "192.168.1.169"
SERVER_PORT = 48084

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка к определенному IP и порту
server_socket.bind((SERVER_IP, SERVER_PORT))

# Начало прослушивания запросов
server_socket.listen()

print(f"Слушаю порт {SERVER_PORT}, ожидаю соединения...")

try:
    while True:
        # Принятие входящего соединения
        connection, address = server_socket.accept()
        with connection:
            print(f"Установлено соединение с {address}.")

            # Получаем данные от клиента
            while True:
                received_data = connection.recv(1024).decode().strip()
                if not received_data or received_data.lower() == "quit":
                    break
                print(f"Сообщение от клиента: {received_data}")

                # Просим пользователя ввести ответ
                answer = input("Введите ответ клиенту: ")

                # Отправляем ответ клиенту
                connection.send(answer.encode('utf-8'))

except KeyboardInterrupt:
    pass

finally:
    server_socket.close()
    print("\nРабота сервера завершена.")

