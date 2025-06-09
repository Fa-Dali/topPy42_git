# cars.py
'''
Определяет конкретные классы транспортных средств,
которые используют абстрактные классы из файла
abstract_classes.py
И логические функции из файла
Logic.py
'''

from abstract_classes import ICar
from logic import Logic

# Общий родительский класс для всех автомобилей
class Car(ICar, Logic):
    def __init__(self,
                 name: str = "",
                 price: int = 0,
                 color: str = "",
                 power: float = 0.0):
        self.name = name
        self.price = price
        self.color = color
        self.power = power

    def display_info(self):
        print(f"=====================================")
        print(f"Автомобиль: {self.name} : "
              f"{self.price:,.2f}".replace(',', ' ') + "рублей.")
        print(f"  Мощность: {self.power} л.с.")
        print(f"  Цвет    : {self.color}")
        print(f"=====================================")

    def configure_vehicle(self):
        raise NotImplementedError("Должен быть реализован в подклассах")


class Sedan(Car):
    def __init__(self,
                 auto_transmission=False,
                 addition_options=False):
        super().__init__(name="", price=0, color="", power=0)
        self.auto_transmission = auto_transmission
        self.additional_options = addition_options

    def display_info(self):
        super().display_info()
        print(f"  Коробка передач     :"
              f" {'Автоматическая' if self.auto_transmission else 'Механическая'}")
        print(f"  Дополнительные опции:"
              f" {'Есть' if self.additional_options else 'Нет'}")

    def configure_vehicle(self):
        self.name = input("Название автомобиля: ")
        self.price = int(input("Цена автомобиля: "))
        self.color = input("Цвет автомобиля: ")
        self.power = float(input("Мощность двигателя: "))
        self.auto_transmission = input("Автоматическая КПП?\n1. "
                                       "Автоматическая\n2. Механическая\n")
        self.additional_options = input("дополнительные опции?\n1. Да\n2. "
                                        "Нет\n")

class OffRoad(Car):
    def __init__(self,
                 framed=False,
                 all_will_drive=False,
                 blocking=False):
        super().__init__(name="", price=0, color="", power=0)
        self.framed = framed
        self.all_will_drive = all_will_drive
        self.blocking = blocking

    def display_info(self):
        super().display_info()
        print(f"  Рамная конструкция: {'Да' if self.framed else 'Нет'}")
        print(f"  Рамная конструкция: {'Да' if self.all_will_drive else 'Нет'}")
        print(f"  Рамная конструкция: {'Да' if self.blocking else 'Нет'}")

    def configure_vehicle(self):
        self.name = input("Название автомобиля: ")
        self.price = int(input("Цена автомобиля: "))
        self.color = input("Цвет автомобиля: ")
        self.power = float(input("Мощность двигателя: "))
        self.framed = input(
            "Рамная конструкция?       :\n1. Да\n2. Нет\n")
        self.all_will_drive = input(
            "Полный привод?            :\n1. Да\n2. Нет\n")
        self.blocking = input(
            "Блокировка дифференциала? :\n1. Да\n2. Нет\n")

class Cargo(Car):
    def __init__(self,
                 tonnage: float = 3.5,
                 installing_trailer: bool = False,
                 sleeping_place: bool = False,
                 number_seats: int = 2):
        super().__init__(name="", price=0, color="", power=0)
        self.tonnage = tonnage
        self.installing_trailer = installing_trailer
        self.sleeping_place = sleeping_place
        self.number_seats = number_seats

    def display_info(self):
        super().display_info()
        print(f"  Грузоподъёмность             : {self.tonnage} тонн")
        print(f"  Возможность установки прицепа: "
              f"{'Да' if self.installing_trailer else 'Нет'}")
        print(f"  Спальное место               : "
              f"{'Да' if self.sleeping_place else 'Нет'}")
        print(f"  Количество мест              : {self.number_seats}")

    def configure_vehicle(self):
        self.name = input("Название автомобиля: ")
        self.price = int(input("Цена автомобиля: "))
        self.color = input("Цвет автомобиля: ")
        self.power = float(input("Мощность двигателя: "))
        self.tonnage = float(input(f"Грузоподъёмность (тонн): "))
        self.installing_trailer = input("Возможность установки "
                                        "прицепа:\n1. Да\n2. Нет\n")
        self.sleeping_place = input("Спальное место:\n1. Да\n2. Нет\n")
        self.number_seats = Logic.counter()