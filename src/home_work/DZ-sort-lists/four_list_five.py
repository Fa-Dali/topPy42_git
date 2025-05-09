'''
Есть четыре списка целых. Необходимо их объединить
в пятом списке. Полученный результат в зависимости от
выбора пользователя отсортировать по убыванию или
возрастанию. Найти значение, введенное пользователем,
с использованием линейного поиска.
'''
list1 = [9, 12, 3, 4, 13]
list2 = [6, 20, 8, 1, 10]
list3 = [11, 2, 5, 14, 18]
list4 = [16, 17, 15, 19, 7]

def sorting_up(list5):
    if not list5:
        print(f"Лист не имеет чисел.")
        return

    list_num = list5
    len_list = len(list_num)
    steps = 0
    for step in range(len_list - 1):
        steps_0 = 0
        for sorting in range(len_list - 1 - step):
            if list_num[sorting + 1] < list_num[sorting]:
                list_num[sorting + 1], list_num[sorting] = list_num[
                    sorting], list_num[sorting + 1]
                steps_0 += 1
        if steps_0 == 0:
            break

        steps += steps_0

    print(f"Список по возрастанию: {list_num}")

def sorting_down(list5):
    if not list5:
        print(f"Лист не имеет чисел.")
        return

    list_num = list5
    len_list = len(list_num)
    steps = 0
    for step in range(len_list - 1):
        steps_0 = 0
        for sorting in range(len_list - 1 - step):
            if list_num[sorting + 1] > list_num[sorting]:
                list_num[sorting + 1], list_num[sorting] = list_num[
                    sorting], list_num[sorting + 1]
                steps_0 += 1
        if steps_0 == 0:
            break

        steps += steps_0

    print(f"Список по убыванию: {list_num}")

def menu():
    list5 = list1 + list2 + list3 + list4
    print(list5)
    print("1 : Сортировка по возрастанию.")
    print("2 : Сортировка по убыванию.")
    print("3 : Оригинальный список")
    while True:
        us_inp = input()
        if us_inp == '1':
            sorting_up(list5)
        elif us_inp == '2':
            sorting_down(list5)
        elif us_inp == '3':
            print(list5)
        else:
            break

def main():
    print("Есть 4 списка:")
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    while True:
        us_inp = input("\nОткрыть меню     : 1"
                       "\nЗакрыть программу: Enter\n")
        if us_inp == '':
            break
        else: menu()

if __name__ == "__main__":
    main()