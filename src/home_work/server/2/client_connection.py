import threading
import socket
import errno

class ClientConnection(threading.Thread):
    __ThreadStop = False
    __mutexLocker = threading.Lock()

    __client_socket = None
    __pool_message_for_sending = []

    __client_name = ""

    def stop_thread(self):
        """Остановка потока"""
        with self.__mutexLocker:
            self.__ThreadStop = True

    def __init__(self, client_socket, broadcast_func, kill_function):
        super().__init__()
        self.__client_socket = client_socket
        self.__client_socket.settimeout(10)
        self.broadcast = broadcast_func
        self.kill_me_please = kill_function

    def get_client_name(self):
        return self.__client_name

    def add_message_for_sending(self, message):
        """Добавляем сообщение в пул отправки"""
        with self.__mutexLocker:
            self.__pool_message_for_sending.append(message)

    def run(self):
        """Основной рабочий цикл потока"""
        while not self.__ThreadStop:
            # Проверяем наличие сообщений для отправки этому клиенту
            with self.__mutexLocker:
                if self.__pool_message_for_sending:
                    messages_to_send = self.__pool_message_for_sending[:]
                    self.__pool_message_for_sending.clear()

            for msg in messages_to_send:
                try:
                    self.__client_socket.send(msg.encode())
                except (OSError, BrokenPipeError):
                    pass  # игнорируем ошибку отправки, возможно, клиент
                    # ужзе вышел.

            # Получаем новые сообщения от клиента
            try:
                data_binary = self.__client_socket.recv(1024)
                if not data_binary:
                    raise ConnectionResetError("Клиент отключился") # принудительно завершить поток

                message = data_binary.decode().strip()
                if not self.__client_name:
                    self.__client_name = message.strip()
                    self.broadcast(self.__client_name, f"{self.__client_name} "
                                                       f"присоединился к "
                                                       f"чату.")
                else:
                    self.broadcast(self.__client_name,
                                   f"{self.__client_name}: {message}")

            except socket.timeout:
                continue
            except (errno.EAGAIN, errno.EWOULDBLOCK):
                continue
            except Exception as e:
                print(f"Произошла ршибка {e}")
                break

        # Завершаем работу клиента
        if self.__client_socket:
            self.__client_socket.close()
