'''Необходимо отсортировать первые две трети списка
в порядке возрастания, если среднее арифметическое
всех элементов больше нуля; иначе — лишь первую треть.
Остальную часть списка не сортировать, а расположить
в обратном порядке.'''
import random

def random_list():
    size_random = int(input("Введите размер списка: \n"))
    min_rndm = int(-(size_random / 2))
    max_rndm = int(size_random / 2)

    rndm_list = []
    print("Формируется список:")
    for _ in range(size_random):
        num = random.randint(min_rndm, max_rndm)
        rndm_list.append(num)
        process_print = len(rndm_list) / 100
        list_proc = []


    print(rndm_list)
    return rndm_list

def sorted_f():
    rndm_list = random_list()
    n = len(rndm_list)
    average = sum(rndm_list) / n if n > 0 else 0

    if average > 0:
        sort_limit = int(n * (2/3))
    else:
        sort_limit = int(n * (1/3))

    sorted_part = sorted(rndm_list[:sort_limit])

    if sort_limit < n:
        reversed_part = rndm_list[sort_limit:][::-1]
    else:
        reversed_part = []

    result = sorted_part + reversed_part
    return result

def main():
    while True:
        us_inp = input("Запускаем процесс?\n1 - Да\nEnter - Выход\n")
        if us_inp == '1':
            print("Результат", sorted_f())
        else:
            break

if __name__ == "__main__":
    main()