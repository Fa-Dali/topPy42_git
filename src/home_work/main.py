def update_menu(menu):
    # Запрашиваем название раздела меню
    section_name = input("Введите название раздела меню: ")

    # Создаем новый раздел
    if section_name not in menu:
        menu[
            section_name] = {}  # Инициализируем пустой словарь для блюд в этом разделе

    # Запрашиваем блюда и их детали
    while True:
        dish_name = input(
            f"Введите название блюда (или 'exit' для выхода из раздела '{section_name}'): ")
        if dish_name.lower() == 'exit':
            break

        description = input("Введите описание блюда: ")
        composition = input("Введите состав блюда: ")
        volume = input("Введите объем блюда: ")

        # Пытаемся получить стоимость как число
        while True:
            price_input = input(
                "Введите стоимость блюда (число без единиц измерения): ")
            try:
                price = float(price_input)  # Пробуем преобразовать в число
                break  # Если успешно, выходим из цикла
            except ValueError:
                print(
                    "Пожалуйста, введите корректное числовое значение. Например: 250")

        # Добавляем блюдо в раздел
        menu[section_name][dish_name] = {
            "Описание": description,
            "Состав": composition,
            "Объем": volume,
            "Стоимость": price
        }
        print(f"Блюдо '{dish_name}' добавлено в раздел '{section_name}'.")


def print_menu(menu):
    if menu:
        print("Текущее Меню:")
        for section, dishes in menu.items():
            print(f"{section}:")
            for dish, details in dishes.items():
                print(f"  - {dish}:")
                print(f"    Описание: {details['Описание']}")
                print(f"    Состав: {details['Состав']}")
                print(f"    Объем: {details['Объем']} мл")
                print(f"    Стоимость: {details['Стоимость']} р.")
    else:
        print("Меню пусто")


def main():
    '''Составление списка меню'''
    menu = {}  # Создаем словарь для хранения меню

    while True:
        us_inp = input("Добавить в меню раздел\n"
                       " Да           : 1\n"
                       " Нет          : 0\n"
                       " Вывести Меню : =\n")  # Изменили на input()

        if us_inp == '1':  # Добавляем раздел
            update_menu(menu)
        elif us_inp == '0':  # Завершаем цикл, если пользователь ответил 'Нет'
            break
        elif us_inp == '=':  # Печатаем текущее меню
            print_menu(menu)
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
