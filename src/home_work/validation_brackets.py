def valid(us_inp):
    simb_a = 0  # (
    simb_b = 0  # {
    simb_c = 0  # [
    tabl_simb = ["", "", ""]
    stack = []

    # Проверка на полноту набора пар символов () [] {}
    if len(us_inp) % 2 != 0:
        print("У вас не полный набор пар символов")
        return

    # Проверка на содержание правильных символов в запросе пользователя
    for i in us_inp:
        if i not in "(){}[]":
            print("НЕКОРРЕКТНЫЙ ВВОД !!!\nМожно использовать: ( ) [ ] { }")
            return

    # Проверка на правильное начало строки запроса пользователя
    if us_inp[0] in ")}]":
        print("Неправильный ввод:\nНачало строки начинается с "
              "закрывающей скобки.\nЭТО НЕ ПРАВИЛЬНО !!!")
        return

    # Процесс анализа
    for simb in range(len(us_inp)):
        if us_inp[simb] == "(":
            simb_a += 1
            stack.append("(")
            tabl_simb[0] = simb_a
        elif us_inp[simb] == "{":
            simb_b += 1
            stack.append("{")
            tabl_simb[1] = simb_b
        elif us_inp[simb] == "[":
            simb_c += 1
            stack.append("[")
            tabl_simb[2] = simb_c
        elif us_inp[simb] == ")":
            if len(stack) == 0:
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n В строке лишняя )")
                return
            last_open = stack.pop()
            if last_open != "(":
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n"
                      "Неправильная последовательность скобок")
                return
            simb_a -= 1
        elif us_inp[simb] == "}":
            if len(stack) == 0:
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n В строке лишняя }")
                return
            last_open = stack.pop()
            if last_open != "{":
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n"
                      "Неправильная последовательность скобок")
                return
            simb_b -= 1
        elif us_inp[simb] == "]":
            if len(stack) == 0:
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n В строке лишняя ]")
                return
            last_open = stack.pop()
            if last_open != "[":
                print("НЕКОРРЕКТНЫЙ ВВОД !!!\n"
                      "Неправильная последовательность скобок")
                return
            simb_c -= 1

    if simb_a == 0 and simb_b == 0 and simb_c == 0:
        print("*** ВАША ЗАПИСЬ ВЕРНАЯ ***")
    if simb_a > 0:
        print("НЕКОРРЕКТНЫЙ ВВОД !!!\nВ строке лишние (", simb_a, "шт.")
    if simb_b > 0:
        print("НЕКОРРЕКТНЫЙ ВВОД !!!\nВ строке лишние {", simb_b, "шт.")
    if simb_c > 0:
        print("НЕКОРРЕКТНЫЙ ВВОД !!!\nВ строке лишние [", simb_c, "шт.")

def main():
    while True:
        us_inp = input("Введите строку скобок в любом порядке, соблюдая\n "
                       "правила пересечения областей действия скобок: \n")
        valid(us_inp)
        if us_inp == "":
            break

if __name__ == "__main__":
    main()