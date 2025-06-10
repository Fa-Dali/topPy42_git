from user_menu import *


def company_menu(price_manager):
    while True:
        print("\nМеню компании:")
        print("1. Редактировать прайс")
        print("2. Показать текущий прайс")
        print("3. Вернуться назад")
        choice = input("Ваш выбор: ")

        if choice == "1":
            edit_pricing(price_manager)
        elif choice == "2":
            show_current_pricing(price_manager)
        elif choice == "3":
            break
        else:
            print("Неправильный ввод. Попробуйте снова.")

def edit_pricing(price_manager):
    print("\nРедактирование прайса:")
    print("Доступные позиции:")
    for idx, item in enumerate(price_manager.prices.keys()):
        print(f"{idx+1}. {item}")
    new_item = input("Введите новое наименование товара или услуги: ")
    new_price = float(input("Цена за единицу: "))
    price_manager.set_price(new_item, new_price)
    print("Изменения успешно сохранены.")