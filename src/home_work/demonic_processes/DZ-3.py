'''
Задание
Пользователь с клавиатуры вводит
- путь к существующей директории
- путь к новой директории

После чего запускается поток, который должен
- скопировать содержимое директории в новое место.
        Необходимо сохранить структуру директории.

На экран необходимо отобразить статистику выполненных операций.
'''

import shutil
import os
import threading
from datetime import datetime

# Класс для копирования директории
class CopyDirectoryThread(threading.Thread):
    def __init__(self, src_dir, dest_dir):
        super().__init__()
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def run(self):
        try:
            # Копируем дерево директорий
            shutil.copytree(self.src_dir, self.dest_dir)
            print(f"Копирование завершено.\nИсходная директория: {self.src_dir}")
            print(f"Цель: {self.dest_dir}")

            # Определяем количество скопированных файлов и папок
            total_files = sum([len(files) for _, _, files in os.walk(self.dest_dir)])
            total_dirs = len([d for d in os.listdir(self.dest_dir) if os.path.isdir(os.path.join(self.dest_dir, d))])

            print(f"\nКоличество скопированных файлов: {total_files}")
            print(f"Количество созданных папок: {total_dirs}")
        except Exception as e:
            print(f"Ошибка копирования: {e}")

# Основная программа
if __name__ == "__main__":
    # Получение путей от пользователя
    source_directory = input("Введите путь к исходной директории: ").strip()
    destination_directory = input("Введите путь к целевой директории: ").strip()

    # Создание и запуск потока
    copy_thread = CopyDirectoryThread(source_directory, destination_directory)
    copy_thread.start()
    copy_thread.join()

    print("Работа программы завершена.")