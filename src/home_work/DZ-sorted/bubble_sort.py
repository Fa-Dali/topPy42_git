'''Написать программу, реализующую сортировку списка
методом усовершенствованной сортировки пузырьковым
методом. Усовершенствование состоит в том, чтобы
- анализировать количество перестановок на каждом шагу,
-- если это количество равно нулю, то продолжать сортировку
нет смысла — список отсортирован.'''

import random
import time

def random_list():
    '''Составление рандомного листа'''
    min_num = int(input("Введите минимальный порог чисел: "))
    max_num = int(input("Введите максимальный порог чисел: "))
    count = int(input("Введите количество случайных чисел: "))

    list_nums = []
    for _ in range(count):
        list_nums.append(random.randint(min_num, max_num))
    print("Сгенерированный список:\n", list_nums)

    return list_nums

def bubble_sorting(list_nums):
    '''Сортировка методом пузырька'''
    line_nums = len(list_nums)
    steps = 0
    steps_time = 0.0

    # Начинаем отсчет времени
    start_time = time.perf_counter()

    for step_line in range(line_nums - 1):
        steps_0 = 0
        for sorting in range(line_nums - 1 - step_line):
            if list_nums[sorting + 1] < list_nums[sorting]:
                list_nums[sorting], list_nums[sorting + 1] = list_nums[
                    sorting + 1], list_nums[sorting]
                steps_0 += 1
                steps += 1

        if steps == 0:
            break

    # Завершаем отсчет времени
    end_time = time.perf_counter()
    steps_time = end_time - start_time  # Общее время сортировки

    print("Отсортированный список:\n", list_nums)
    print(f"Выполнено {steps} шагов перестановки.\n")

    if steps > 0:
        average_swap_time = steps_time / steps
        minuts = steps / steps_time
        print(f"Среднее время перестановки: {average_swap_time:.10f} секунд\n"
              f"Общее время               : {steps_time:.5f}      секунд.\n"
              f"Скорость операций в минуту: {minuts:.2f}")
    else:
        print("Перестановок не было. Среднее время 0 секунд.")

def menu():
    while True:
        print("_________МЕНЮ___________")
        print("Выход ...... [Enter]:")
        print("Сортировка пузырьком: 1")
        print("")

        us_inp = input("Выберите пункт меню: ")
        print("_________****___________")

        if us_inp == '1':
            numbers = random_list()
            bubble_sorting(numbers)

        elif us_inp == "":
            print("\nВыполнение программы закончено.")
            break
        else:
            print("\nНе верный ввод. Повторите")

def main():
    menu()

if __name__ == "__main__":
    main()

