import sys
from time import sleep

class Logic:
    @staticmethod
    def toggle_attribute(obj, attr_name):
        current_value = getattr(obj, attr_name)
        new_value = not current_value
        setattr(obj, attr_name, new_value)
        return new_value

    @staticmethod
    def clear_last_line(lines=1):
        '''очистка прошлой строки'''
        for _ in range(lines):
            sys.stdout.write('\x1b[1A')  # перемещаем курсор вверх
            sys.stdout.write('\x1b[2K')  # очищение текущей строки

    @staticmethod
    def quantity():
        '''выбор количества спальных мест'''
        var_bool = False
        vb = 1
        while True:
            print(f"Добавьте необходимое количество: {vb}")
            print("-> Пробел : добавить / убавить ")
            print("-> Ввод   : утвердить ")
            us_inp = input("===================\n")

            if us_inp == ' ':
                var_bool = not var_bool
                if vb == 1:
                    vb = 2
                    print(f": {vb} спалных места.")
                elif vb == 2:
                    vb = 1
                    print(f": {vb} спалное место.")

            elif us_inp == '':
                break

        return 1 if var_bool else 2

    @staticmethod
    def counter():
        '''счетчик увеличения/уменьшения количества с установленным
        ограничением от 2 до 7 мест'''

        print("Счетчик увеличения <-> уменьшения количества:\n"
              "   + : добавить\n"
              "   - : убавить\n"
              "-------------------\n"
              "Ввод : Подтвердить\n"
              "===================\n")
        count = 2
        print("Количество мест : ", count, " мест\n")
        while True:
            us_inp = input()
            if us_inp == '':
                break

            elif us_inp == '+':
                if count < 7:
                    count += 1
                Logic.clear_last_line(2)
                print("Количество мест : ", count, " мест\n")

            elif us_inp == '-':
                if 2 < count:
                    count -= 1
                Logic.clear_last_line(2)
                print("Количество мест : ", count, " мест\n")

            else:
                Logic.clear_last_line(3)
                print("Некорректный ввод.\n"
                      "Повторите или Подтвердите выбор.")

        return count


class Car(Logic):
    def __init__(self, name: str = "", price: int = 0, color: str = "",
                 power: float = 0.0):
        self.name = name
        self.price = price
        self.color = color
        self.power = power

    def __str__(self):
        return (f"Автомобиль: {self.name} : {self.price} рублей."
                 f"\nМощность: {self.power}\nЦвет: {self.color}")


class Sedan(Car):
    '''
    - седан:   .......................sedan
    1.  АКПП - .......................auto_transmission
        МКПП - .......................manual_transmission
    2. кол-во дополнительных опций - additional_options
    '''

    def __init__(self,
                 auto_transmission=False,
                 additional_options=False):
        super().__init__(name="", price=0, color="", power=0)
        self.auto_transmission = auto_transmission
        self.additional_options = additional_options

    # Выбирает опцию МККП/АКПП : bool
    def transmission(self):
        self.auto_transmission = not self.auto_transmission

    # Выбирает доп_опции : bool
    def add_option(self):
        self.additional_options = not self.additional_options

    def __str__(self):
        return (f"\nАвто Седан\n"
                f"===============================\n"
                f"Коробка передач .... : "
                f"{'Механика' if not self.auto_transmission else 'Автомат'}\n"
                f"Дополнительные опции : "
                f"{'Нет' if not self.additional_options else 'Есть'}")


class OffRoad(Car):
    '''
    - внедорожник:    ................off-road vehicle
    1. рамный или нет ................framed
    2. полный привод  ................all_wheel_drive
    3. блокировка     ................blocking
    '''

    def __init__(self,
                 framed=False,
                 all_wheel_drive=False,
                 blocking=False):
        super().__init__(name="", price=0, color="", power=0)
        self.framed = framed
        self.all_wheel_drive = all_wheel_drive
        self.blocking = blocking

    # Рамная конструкция : bool
    def swich_fram(self):
        self.framed = not self.framed

    # Полный привод : bool
    def all_drive(self):
        self.all_wheel_drive = not self.all_wheel_drive

    # блокировка : bool
    def switch_blockinging(self):
        self.blocking = not self.blocking

    def __str__(self):
        return (f"\nАвто Внедорожник\n"
                f"===============================\n"
                f"Рамная конструкция : "
                f"{'Стандарт' if not self.framed else 'Усилена'}\n"
                f"Полный привод .... : "
                f"{'+' if not self.all_wheel_drive else '-'}\n"
                f"Блокировка ....... : "
                f"{'+' if not self.blocking else '-'}")


class Cargo(Car):
    '''
    - грузовой .......................cargo
    1. тоннаж  .......................tonnage
    2. возможность установки прицепа .installing_trailer
    3. наличие спального места .......sleeping_place
    4. кол-во мест             .......number_seats
    '''

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

    # Возможность установки прицепа
    def install_trailer(self):
        self.installing_trailer = not self.installing_trailer

    # Выбор кол-ва мест для сна
    def sleep_place(self):
        selected_places = Logic.quantity()
        return selected_places

    # количество мест
    def set_number_seats(self):
        seats_count = Logic.counter()
        self.number_seats = seats_count
        return seats_count

    def __str__(self):
        return (f"\nАвто Грузовик\n"
                f"===============================\n"
                f"Грузоподъемность .............. : {self.tonnage} тонн\n"
                f"Возможность установки прицепа .. : "
                f"{'Есть' if self.installing_trailer else 'Нет'}\n"
                f"Наличие спального места ........ : "
                f"{'Есть' if self.sleeping_place else 'Нет'}\n"
                f"Количество мест ................. : {self.number_seats}")


# Основной сценарий
if __name__ == "__main__":
    # Пользовательские запросы
    print("Создание нового автомобиля...")
    name = input("Название автомобиля: ")
    price = int(input("Цена автомобиля: "))
    color = input("Цвет автомобиля: ")
    power = float(input("Мощность двигателя: "))

    # Вопросы для создания определенного типа автомобиля
    print("Какой тип автомобиля?")
    print("[1] Седан")
    print("[2] Внедорожник")
    print("[3] Грузовик")
    choice = input("Ваш выбор: ")

    if choice == '1':
        car = Sedan(auto_transmission=input("Автоматическая КПП? (Y/N): ") == 'Y',
                   additional_options=input("Дополнительные опции? (Y/N): ") == 'Y')
        car.name = name
        car.price = price
        car.color = color
        car.power = power
        print(car)
    elif choice == '2':
        car = OffRoad(framed=input("Рамная конструкция? (Y/N): ") == 'Y',
                     all_wheel_drive=input("Полный привод? (Y/N): ") == 'Y',
                     blocking=input("Система блокировки? (Y/N): ") == 'Y')
        car.name = name
        car.price = price
        car.color = color
        car.power = power
        print(car)
    elif choice == '3':
        car = Cargo(tonnage=float(input("Грузоподъемность (тонн): ")),
                  installing_trailer=input("Возможно подключение прицепа? (Y/N): ") == 'Y',
                  sleeping_place=input("Имеется спальное место? (Y/N): ") == 'Y',
                  number_seats=int(input("Количество мест: ")))
        car.name = name
        car.price = price
        car.color = color
        car.power = power
        print(car)
    else:
        print("Некорректный выбор типа автомобиля.")