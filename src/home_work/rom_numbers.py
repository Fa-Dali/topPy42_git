def valid(us_string):
    rim_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100
    }

    for i in range(len(us_string)):
        if us_string[i] not in rim_dict:
            print("Не корректный ввод. Повторите.")
            return

    us_list = list(reversed(us_string))
    print(us_list)
    result = rim_dict[us_list[0]]

    for number in range(len(us_list)):
        number_next = number + 1
        if number_next == len(us_list):
            print(us_string, " = ", result)
            print("Рассчёт закончен.")
        else:
            num_a = rim_dict[us_list[number]]
            num_b = rim_dict[us_list[number_next]]
            if num_a > num_b:
                result -= num_b
            else:
                result += num_b

def main():
    while True:
        us_string = input("------------------------------\n"
                          "Выход из программы -> [Enter] :\n"
                          "ВВЕДИТЕ РИМСКОЕ ЧИСЛО         :\n")
        valid(us_string)
        if us_string == "":
            break


if __name__ == "__main__":
    main()