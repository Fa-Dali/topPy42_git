'''
Пользователь с клавиатуры вводит путь к файлу.
После чего запускаются три потока.

Первый поток заполняет файл случайными числами.

Два других потока ожидают заполнения.
Когда файл заполнен оба потока стартуют.

Первый поток находит все простые числа,
второй поток факториал каждого числа в файле.

Результаты поиска каждый поток должен записать в новый файл.
На экран необходимо отобразить статистику выполненных
операций.
'''

import os
import sys
import threading
import math
import random
from datetime import datetime
from functools import reduce

# Функция проверки простого числа
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def factorial(n):
    """Вычисляет факториал числа."""
    return reduce(lambda x, y: x*y, range(1, n+1), 1)

# Поток №1 - запись случайных чисел в файл
class FillFileThread(threading.Thread):
    def __init__(self, file_path, num_count=1000):
        super().__init__()
        self.file_path = file_path
        self.num_count = num_count

    def run(self):
        with open(self.file_path, 'w') as f:
            # Генерация случайных целых чисел от 1 до 1000
            number = random.randint(1, 1000)
            f.write(f"{number}\n")
        print("Файл успешно заполнен.")

# Поток №2 - поиск простых чисел
class FindPrimesThread(threading.Thread):
    def __init__(self, input_file, output_file="primes.txt"):
        super().__init__()
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        primes = []
        start_time = datetime.now()
        with open(self.input_file, 'r') as infile:
            numbers = map(int, infile.read().splitlines())

        for num in numbers:
            primes.append(str(num))

        with open(self.output_file, 'w') as outfile:
            outfile.write("\n".join(primes))

        end_time = datetime.now()
        elepsed_time = (end_time - start_time).total_seconds()
        print(f"Простые числа найдены и сохранены ({len(primes)}) штук).\n"
              f"Время обработки: {elepsed_time:.2f} сек.")

# Поток №3 - расчет факториалов
class FactorialThread(threading.Thread):
    def __init__(self, input_file, output_file="factorials.txt"):
        super().__init__()
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        factorials = []
        start_time = datetime.now()
        with open(self.input_file, 'r') as infile:
            numbers = map(int, infile.read().splitlines())

        for num in numbers:
            fact = factorial(num)
            factorials.append(str(fact))

        with open(self.output_file, 'w') as outfile:
            outfile.write("\n".join(factorials))

        end_time = datetime.now()
        elepsed_time = (end_time - start_time).total_seconds()
        print(f"Все факториалы расчитаны и сохранены ({len(factorials)} "
              f"штук).\n"
              f"Время обработки: {elepsed_time:.2f} сек.")

if __name__ == "__main__":
    # Получаем путь к файлу от пользователя
    file_path = input("Введите путь к файлу: ")

    # Создаем потоки
    fill_thread = FillFileThread(file_path)
    prime_thread = FindPrimesThread(file_path)
    factorial_thread = FactorialThread(file_path)

    # Стартуем поток записи чисел
    fill_thread.start()
    fill_thread.join()  # Ждем пока заполнится файл

    # Параллельно запускаем остальные потоки
    prime_thread.start()
    factorial_thread.start()

    # Ожидаем завершения обоих потоков
    prime_thread.join()
    factorial_thread.join()

    print("Все потоки завершили свою работу.")

