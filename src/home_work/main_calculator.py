# import sys
# import os
#
# sys.path.append(os.path.join(os.path.dirname(__file__), '../repos_fibo_new'))

from Projects.top_academy.topPy42_git.repos_fibo_new.main import (
    fibonacci_iterative
as fibonacci_iterative)

def calculate(expression):
    # Убираем лишние пробелы
    expression = expression.replace(" ", "")

    # Обработка сложения и вычитания
    tokens = []
    num = ""
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(float(num))
                num = ""
            tokens.append(char)
    if num:
        tokens.append(float(num))

    # Обработка умножения и деления
    result = []
    i = 0
    while i < len(tokens):
        if tokens[i] in ['*', '/']:
            operator = tokens[i]
            left = result.pop() if result else tokens[i - 1]
            right = tokens[i + 1]
            if operator == '*':
                result.append(left * right)
            elif operator == '/':
                if right == 0:
                    return "Ошибка: Деление на ноль!"
                result.append(left / right)
            i += 1  # Пропустить следующий элемент (число)
        else:
            result.append(tokens[i])
        i += 1

    # Обработка сложения и вычитания
    total = result[0]
    for i in range(1, len(result), 2):
        operator = result[i]
        right = result[i + 1]
        if operator == '+':
            total += right
        elif operator == '-':
            total -= right

    return total


def calculator():
    print("Введите математическое выражение:")
    print("Примеры: 2 + 2, 3 * 4 - 5, 10 / 2")
    print("Введите 'exit' для выхода.")
    print("Для вычисления Фибоначи: F(<номер позиции>) :\n")

    while True:
        user_input = input("Введите выражение: ")

        if user_input.lower() == 'exit':
            print("Выход из калькулятора.")
            break

        if user_input.startswith("F(") and user_input.endswith(")"):
            try:
                n = int(user_input[2: -1])
                result = fibonacci_iterative(n)

                print(f"Число Фибоначи на позиции {n} : {result}")
                continue

            except ValueError:
                print("Ошибка: не верный ввод для чисел Фибоначи.")
                continue

        result = calculate(user_input)
        print(f"Результат: {result}")


if __name__ == "__main__":
    calculator()
