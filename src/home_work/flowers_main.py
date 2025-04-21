# ЧЕРНОВИК:
# i  - счетчик символов :     i +=  1
# j0 - счетчик нулей    :    j0 +=  1
# k - отсечение первого места на клумбе
# if (max_0 < 0) = 0
# if (j0 > max_0) = max_0=j0
#  1  1  0  0  0  1  1
# -1 -1 +1 +1 +1 -1 -1
#    -1  0  1  2

def calculat(flow_place):
    '''
    Поиск максимального места клумбы для посадки группы цветов.
    Условие: края группы новых цветов не должны контактировать с растущими
    цветами на клумбе
    '''
    max_0, i, j0, k = 0, 0, 0, 0
    # Обработка, если строка начинается на 0 : 0001 ...
    for i in range(len(flow_place)):
        if flow_place[i] == '0' and k == 0:
            j0 += 1; k = 1
        else: break

    # Обработка, если строка имеет вид : ... 10001 ...
    for i in range(len(flow_place)):
        if flow_place[i] == '1':
            j0 -= 2
            if j0 > max_0:
                max_0 = j0
            j0 = 0; i += 1
        else:
            j0 += 1; i += 1

    # Обработка, если строка заканчивается на 0 : ... 1000
    if j0 > max_0:
        max_0 = j0 - 1

    return max_0

def is_valid_input(flow_place):
    # Проверяем, чтобы ввод содержал только '0' и '1'
    return all(char in '01' for char in flow_place)

def us_inp():
    while True:
        flow_place = input("Покажите клумбу символами 0 и 1\nнапример : "
                           "010000010\n"
                           "Выход из программы : Enter\n"
                           "-------------------------------\n")
        if flow_place == "":
            break

        if not is_valid_input(flow_place):
            print(
                "Ошибка: допускаются только символы '0' и '1'. Попробуйте снова.")
            continue  # Идём на следующую итерацию, чтобы запросить ввод снова

        result = calculat(flow_place)
        print(f"Ответ:\n  Требуется {result} шт. цветов.\n"
              f"-------------------------------")

if __name__ == "__main__":
    us_inp()