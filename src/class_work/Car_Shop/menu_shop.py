
import sys
from Car_Shop import *
from Car_Shop import Logic

def show_main_menu():
    """Главное меню"""
    print()
    print("==============================")
    print("*     Авто-конфигурация      *")
    print("==============================")
    print("Выберите тип автомобиля:")
    print("[1]. Седан               :")
    print("[2]. Внедорожник         :")
    print("[3]. Грузовой автомобиль :")
    print("[Q]. Выход               :")

def show_common_settings(car):
    """Общие настройки автомобиля"""
    print()
    print("======================")
    print("|  Общие настройки   |")
    print("===========================")
    print(f"Имя автомобиля    : {car.name}")
    print(f"Цена автомобиля   : {car.price:,}".replace(",", " ") + " рублей")
    print(f"Мощность двигателя: {car.power} л.с.")
    print(f"Цвет кузова       : {car.color}")
    print("---------------------------")
    print("[N] - Имя автомобиля      :")
    print("[P] - Цена автомобиля     :")
    print("[W] - Мощность двигателя  :")
    print("[C] - Цвет кузова         :")
    print("[X] - СПЕЦИФИЧЕСКИЕ ОПЦИИ :")
    action = input("Выберите действие: ").strip().upper()

    if action == 'N':
        car.name = input("Введите имя автомобиля: ")
    elif action == 'P':
        car.price = int(input("Введите цену автомобиля: "))
    elif action == 'W':
        try:
            car.power = float(input("Введите мощность двигателя: "))
        except ValueError:
            print("Некорректный ввод. Введите число.")
            return True
    elif action == 'C':
        car.color = input("Введите цвет автомобиля: ")
    elif action == 'X':
        return False
    else:
        print("Некорректный выбор. Попробуйте снова.")

    return True

def show_config_menu(car):
    """Меню конфигурации для выбранного автомобиля"""
    # clear_screen()
    print("****************************")
    print("* Конфигурация автомобиля  *")
    print("****************************")
    print(str(car))
    print("---------------------------")
    actions = {
        'Sedan': [
            ['T', 'Тип трансмиссии'],
            ['O', 'Дополнительные опции']
        ],
        'OffRoad': [
            ['F', 'Рамная конструкция'],
            ['D', 'Полный привод'],
            ['B', 'Блокировка дифференциала']
        ],
        'Cargo': [
            ['I', 'Установка прицепа'],
            ['S', 'Спальное место'],
            ['N', 'Количество посадочных мест']
        ]
    }

    # Выбираем действия в зависимости от типа автомобиля
    car_class = car.__class__.__name__
    available_actions = actions.get(car_class, [])

    # Показываем доступные опции
    for act_key, desc in available_actions:
        print(f'[{act_key}] - {desc}')
    print('[Q] - Возврат в главное меню')

    action = input("Выберите действие: ").strip().upper()

    if action == 'Q':
        return False
    elif any(act[0] == action for act in available_actions):
        # Выполняем соответствующую операцию
        if action == 'T':
            car.transmission()
        elif action == 'O':
            car.add_option()
        elif action == 'F':
            car.swich_fram()
        elif action == 'D':
            car.all_drive()
        elif action == 'B':
            car.switch_blockinging()
        elif action == 'I':
            car.install_trailer()
        elif action == 'S':
            car.sleep_place()
        elif action == 'N':
            car.set_number_seats()
    else:
        print("Некорректный выбор. Попробуйте снова.")

    return True

def main():
    while True:
        show_main_menu()
        choice = input("Ваш выбор: ").strip().upper()

        if choice == '1':
            car = Sedan()
        elif choice == '2':
            car = OffRoad()
        elif choice == '3':
            car = Cargo()
        elif choice == 'Q':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Выберите из предложенных вариантов.")
            continue

        common_loop = True
        while common_loop:
            common_loop = show_common_settings(car)

        config_loop = True
        while config_loop:
            config_loop = show_config_menu(car)

if __name__ == "__main__":
    main()