import random

def f_process():
    size = int(input("Введите количество чисел\n"))
    min_value = -20
    max_value = 20

    random_nums = []

    for _ in range(size):
        num = random.randint(min_value, max_value)
        random_nums.append(num)

    print("Список чисел: ", random_nums)

    min_element = 0
    max_element = 0
    negative_count = 0
    positive_count = 0
    zero_count = 0

    for number in random_nums:
        if number < 0:
            negative_count += 1
        elif number > 0:
            positive_count += 1
        else:
            zero_count += 1

        if number < min_element:
            min_element = number
        if number > max_element:
            max_element = number

    print(f"Минимальный элемент .......... : {min_element}")
    print(f"Максимальный элемент ......... : {max_element}")
    print(f"Кол-во отрицательных элементов : {negative_count}")
    print(f"Кол-во положительных элементов : {positive_count}")
    print(f"Кол-во нулей ................. : {zero_count}")

def main():
    while True:
        us_inp = input("Запустим процесс?\n 1 - Да\nEnter - Нет\n")
        if us_inp == '1':
            f_process()
        else:
            break

if __name__ == "__main__":
    main()