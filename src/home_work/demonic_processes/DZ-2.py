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
    return reduce(lambda x, y: x*y, range(1, n+1)) if n > 0 else 1

# Основной рабочий код:

