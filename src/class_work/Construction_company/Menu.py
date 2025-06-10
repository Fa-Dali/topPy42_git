
from manager_menu import *
from PriceListManager import *


def main():
    global price_manager
    price_manager = PriceListManager()

    while True:
        print("\nГлавное меню:")
        print("1. Покупатель")
        print("2. Компания")
        print("3. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            customer_menu(price_manager)
        elif choice == "2":
            company_menu(price_manager)
        elif choice == "3":
            break
        else:
            print("Неправильный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()