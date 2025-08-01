'''
При старте приложения запускаются три потока.
Первый поток заполняет список случайными числами.
- И находит сумму элементов списка.
Два других потока ожидают заполнения.
-  второй поток среднеарифметическое значение в списке
Когда список заполнен оба потока запускаются.
Полученный список, сумма и среднеарифметическое выводятся на экран.
'''

import threading
from random import randrange
from time import sleep

# Общий ресурс (список чисел)
numbers = []
lock = threading.Lock()  # Блокировка для безопасного доступа к общему ресурсу
event_filled = threading.Event()  # Сигнал для ожидания окончания заполнения списка

def fill_list():
    global numbers
    print("\nПервый поток начал заполнять список")
    for _ in range(10):
        num = randrange(1, 100)
        with lock:
            numbers.append(num)
        sleep(0.1)
    event_filled.set()  # Сообщаем остальным потокам, что список заполнен
    print("\nСписок заполнен")

def sum_numbers():
    event_filled.wait()  # Ждем сигнала о завершении заполнения
    total_sum = 0
    with lock:
        total_sum = sum(numbers)
    print(f"\nСумма элементов списка: {total_sum}")

def average_numbers():
    event_filled.wait()  # Ждем сигнала о завершении заполнения
    avg_value = 0
    with lock:
        avg_value = sum(numbers) / len(numbers)
    print(f"\nСреднее арифметическое элементов списка: {avg_value:.2f}")

# Запуск трех потоков
thread_fill = threading.Thread(target=fill_list)
thread_sum = threading.Thread(target=sum_numbers)
thread_avg = threading.Thread(target=average_numbers)

# Начинаем выполнение потоков
thread_fill.start()
thread_sum.start()
thread_avg.start()

# Ждем завершения всех потоков
thread_fill.join()
thread_sum.join()
thread_avg.join()

print("Программа завершена")


