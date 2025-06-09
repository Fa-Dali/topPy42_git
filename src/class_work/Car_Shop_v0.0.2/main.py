# main.py
'''
Главная точка входа, где
- создается экземпляр нужного автомобиля и
- выполняется конфигурация
'''

from cars import Sedan, OffRoad, Cargo

print("Создание нового автомобиля")
print("Выберите тип автомобиля:")
print(" - Седан       [1]")
print(" - Внедорожник [2]")
print(" - Грузовик    [3]")
print("==========================")
choice = input("Ваш выбор: ")

if choice == '1':
    car = Sedan()
elif choice == '2':
    car = OffRoad()
elif choice == '3':
    car = Cargo()
else:
    print("Некорректный выбор типа автомобиля.")
    exit()

car.configure_vehicle()
car.display_info()

