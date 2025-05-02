'''
Пользователь вводит с клавиатуры арифметическое
выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция,
число. Возможные операции: +, -,*,/
'''
def calculate_expression(expression):
    expression = expression.replace(" ", "")

    for char in expression:
        if char in '-+/*':
            operator = char
            num1, num2 = expression.split(operator)
            print(f"num1: {num1}\noperator: {operator}\nnum2: {num2}")
            break
    else:
        raise ValueError("Операция не найдена. Пожалуйста, введите выражение "
                         "в формате: число-операция-число")

    num1 = int(num1)
    num2 = int(num2)

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль не допустимо.")
        return num1 / num2


def main():
    while True:
        us_str = input("Введите арифметическое выражение с двумя числами:\n")
        try:
            if us_str == "":
                break

            result = calculate_expression(us_str)
            print(f"Результат: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()