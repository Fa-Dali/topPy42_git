from user_menu import *
from Estimates import *


def customer_menu(price_manager):
    while True:
        print("\nМеню покупателя:")
        print("1. Собрать дом")
        print("2. Посмотреть текущий прайс")
        print("3. Вернуться назад")
        choice = input("Ваш выбор: ")

        if choice == "1":
            build_house(price_manager)
        elif choice == "2":
            show_current_pricing(price_manager)
        elif choice == "3":
            break
        else:
            print("Неправильный ввод. Попробуйте снова.")

def build_house(price_manager):
    house_components = {
        "Подвал": {},
        "Первый этаж": {},
        "Второй этаж": {},
        "Крыша": {},
        "Доп. постройки": {}
    }

    # Циклический ввод данных
    for key in house_components.keys():
        print(f"\nНастройка компонента: {key}")
        if key == "Подвал":
            house_components[key]["area"] = float(input("Площадь подвала (кв.м): "))
        elif key.startswith("Этаж"):
            house_components[key]["area"] = float(input("Площадь этажа (кв.м): "))
            house_components[key]["num_rooms"] = int(input("Количество комнат: "))
            house_components[key]["num_bathrooms"] = int(input("Количество санузлов: "))
        elif key == "Крыша":
            house_components[key]["type"] = input("Тип крыши (односкатная/двухскатная): ")
            house_components[key]["attic"] = input("Чердак (да/нет)? ").strip().lower().startswith("д")
            house_components[key]["satellite_dish"] = input("Спутниковая антенна (да/нет)? ").strip().lower().startswith("д")
        elif key == "Доп. постройки":
            valid_input = False
            while not valid_input:
                try:
                    count = int(input("Сколько дополнительных построек планируете построить? "))
                    valid_input = True
                except ValueError:
                    print("Ошибка: пожалуйста, введите число.")

            buildings = []
            for i in range(count):
                building_type = input(f"Тип постройки #{i+1}: ")
                buildings.append(building_type.strip())
            house_components[key]["types"] = buildings

    # Инициализация калькулятора
    calculator = HomeConfigurator(house_components, price_manager)
    total_cost = calculator.calculate_total_cost()
    print(f"Стоимость Вашего дома составляет: {total_cost:.2f} руб.")

def show_current_pricing(price_manager):
    prices = price_manager.prices
    print("\nТекущие расценки:")
    for item, value in prices.items():
        print(f"- {item}: {value} руб./ед.")