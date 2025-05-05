def input_grades():
    grades = []
    print("Введите 10 оценок студента от 1 до 12:")
    for i in range(10):
        while True:
            try:
                grade = int(input(f"Оценка {i + 1}: "))
                if 1 <= grade <= 12:
                    grades.append(grade)
                    break
                else:
                    print("Оценка должна быть от 1 до 12. Попробуйте еще раз.")
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")
    return grades


def display_grades(grades):
    print("Оценки студента:", grades)


def retake_exam(grades):
    display_grades(grades)
    while True:
        try:
            index = int(input(
                "Введите номер элемента (1-10), который хотите изменить: ")) - 1
            if 0 <= index < len(grades):
                new_grade = int(input(
                    f"Введите новую оценку для элемента {index + 1} (от 1 до 12): "))
                if 1 <= new_grade <= 12:
                    grades[index] = new_grade
                    print("Оценка изменена.")
                    break
                else:
                    print("Оценка должна быть от 1 до 12.")
            else:
                print("Некорректный номер. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")


def scholarship_status(grades):
    average = sum(grades) / len(grades)
    if average >= 10.7:
        print("Стипендия выходит.")
    else:
        print("Стипендия не выходит.")


def sorted_grades(grades):
    order = input(
        "Сортировать по возрастанию (введите 1) или по убыванию (введите 2)? ")
    if order == '1':
        print("Сортированный список по возрастанию:", sorted(grades))
    elif order == '2':
        print("Сортированный список по убыванию:",
              sorted(grades, reverse=True))
    else:
        print("Некорректный ввод.")


def main():
    grades = input_grades()

    while True:
        print("\nМеню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Выходит ли стипендия")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            display_grades(grades)
        elif choice == '2':
            retake_exam(grades)
        elif choice == '3':
            scholarship_status(grades)
        elif choice == '4':
            sorted_grades(grades)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
