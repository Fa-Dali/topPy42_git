# logic.py
import sys
from time import sleep


class Logic:

    '''Логическое True <-> False'''
    @staticmethod
    def toggle_attribute(obj, attr_name):
        current_value = getattr(obj, attr_name)
        new_value = not current_value
        setattr(obj, attr_name, new_value)
        return new_value

    '''очистка прошлой строки'''
    @staticmethod
    def clear_last_line(lines=1):
        for _ in range(lines):
            sys.stdout.write('\x1b[1A')  # перемещаем курсор вверх
            sys.stdout.write('\x1b[2K')  # очищение текущей строки

    '''выбор количества спальных мест'''
    @staticmethod
    def quantity():
        var_bool = False
        vb = 1
        while True:
            print(f"Добавьте необходимое количество: {vb}")
            print("-> Пробел : добавить / убавить ")
            print("-> Ввод   : утвердить ")
            us_inp = input("===================\n")

            if us_inp == ' ':
                var_bool = not var_bool
                if vb == 1:
                    vb = 2
                    print(f": {vb} спалных места.")
                elif vb == 2:
                    vb = 1
                    print(f": {vb} спалное место.")

            elif us_inp == '':
                break

        return 1 if var_bool else 2

    '''счетчик увеличения/уменьшения количества с установленным
            ограничением от 2 до 7 мест'''
    @staticmethod
    def counter():
        print("Счетчик увеличения <-> уменьшения количества:\n"
              "   + : добавить\n"
              "   - : убавить\n"
              "-------------------\n"
              "Ввод : Подтвердить\n"
              "===================\n")
        count = 2
        print("Количество мест : ", count, " мест\n")
        while True:
            us_inp = input()
            if us_inp == '':
                break

            elif us_inp == '+':
                if count < 7:
                    count += 1
                Logic.clear_last_line(2)
                print("Количество мест : ", count, " мест\n")

            elif us_inp == '-':
                if 2 < count:
                    count -= 1
                Logic.clear_last_line(2)
                print("Количество мест : ", count, " мест\n")

            else:
                Logic.clear_last_line(3)
                print("Некорректный ввод.\n"
                      "Повторите или Подтвердите выбор.")

        return count
