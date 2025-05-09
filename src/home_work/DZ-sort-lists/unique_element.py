'''
Есть четыре списка целых. Необходимо объединить
в пятом списке только те элементы,
- которые уникальны для каждого списка.
Полученный результат в зависимости от выбора пользователя
- отсортировать по убыванию или возрастанию.
- Найти значение, введенное пользователем, с использованием бинарного поиска.
'''

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [7, 8, 9, 10, 11]
list4 = [10, 11, 12, 13, 14]


def find_unique_elements(*lists):
    unique_elements = []
    for lst in lists:
        current_set = set(lst)
        for element in current_set:
            is_unique = True
            for other_lst in lists:
                if other_lst != lst and element in other_lst:
                    is_unique = False
                    break
            if is_unique:
                unique_elements.append(element)

    return unique_elements


unique_list = find_unique_elements(list1, list2, list3, list4)

sort_option = input("Введите\n'1' для сортировки по возрастанию\n'2' для "
                    "сортировки по убыванию")
if sort_option == '1':
    unique_list.sort()
if sort_option == '2':
    unique_list.sort(reverse=True)
else:
    print("Некорректный ввод. Список остается без изменений.")

print(f"Уникальные элементы: {unique_list}")


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if unique_list:
    try:
        us_inp = int(input("Введите число для поиска: "))
        index = binary_search(unique_list, us_inp)

        if index != -1:
            print(f"Число {us_inp} найдено на позиции {index + 1}.")
        else:
            print(f"Число {us_inp} не найдено.")
    except ValueError:
        print("Пожалуйста, введите целое число.")
else:
    print("Список уникальных элементов пуст.")