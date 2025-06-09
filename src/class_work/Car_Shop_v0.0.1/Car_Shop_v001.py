'''
На завод по производству автомобилей необходимо создать
систему классов для ведения базы данныхвсех выпущенных авто.
Все автомобили обладают необходимыми характеристиками:

Car
1 цена -     .....................price
2 название - .....................name
3 цвет -     .....................color
4 мощность - .....................power

Необходимо реализовать классы для следующих видов машин:

Sedan
- седан:   .......................sedan
1.  АКПП - .......................auto_transmission
    МКПП - .......................manual_transmission
2. кол-во дополнительных опций - additional_options

OffRoad
- внедорожник:    ................off-road vehicle
1. рамный или нет ................framed
2. полный привод  ................all_wheel_drive
3. блокировка     ................blocking

Cargo
- грузовой
1. тоннаж
2. возможность установки прицепа .installing_trailer
3. наличие спального места .......sleeping place
4. кол-во мест             .......number_seats
'''
import  sys
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
            sys.stdout.write('\x1b[1A') # перемещаем курсор вверх
            sys.stdout.write('\x1b[2K')  # очищение текущей строки

    @staticmethod
    def quantity():
        '''Выбор количества мест для сна'''

        var_bool = False
        vb = 1
        while True:
            print(f"Добавьте необходимое количество: {vb}")
            print("-> Пробел : добавить / убавить ")
            print("-> Ввод   : утвердить ")
            # print("===================")
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
    def __init__(self, name: str = ".....", price: int = 0, color: str =
    "черный", power: float = 0.0):
        self.name = name
        self.price = price
        self.color = color
        self.power = power

    def name_car(self):
        return self.name

    def price_car(self):
        return f"{self.price:,2d}"

    def color_car(self):
        return self.color

    def power_car(self):
        return self.power

    # def __repr__(self):
    #     return (
    #         f"{self.__class__.__name__}(name='{self.name}', price={self.price}, "
    #         f"color='{self.color}', power={self.power})"
    #     )

    def __str__(self):
        return (f"Автомобиль: {self.name} : {self.price} рублей."
                 f"\nМощность: {self.power}\nЦвет: {self.color}")

    def __del__(self):
        pass


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

        super().__init__( name="",price=0, color="", power=0)
        self.auto_transmission = auto_transmission
        self.additional_options = additional_options

    # Выбирает опцию МККП/АККП : bool
    def transmission(self):
        '''
        Опция: МККП -> False
               АККП -> True
        '''
        # option_transmission = self.toggle_attribute(self, 'auto_transmission')
        # return option_transmission
        self.auto_transmission = not self.auto_transmission

    # Выбырает доп_опции : bool
    def add_option(self):
        '''
        Опция: нет -> False
               есть -> True
        '''
        # add_options = self.toggle_attribute(self, 'additional_options')
        # return add_options
        self.additional_options = not self.additional_options

    def __str__(self):
        return (f"\nАвто Седан\n"
                f"===============================\n"
                f"Коробка передач .... : "
                f"{'Механика' if not self.auto_transmission else 'Автомат'}\n"
                f"Дополнительные опции : "
                f"{'Нет' if not self.additional_options else 'Есть'}")

    def __del__(self):
        pass


class OffRoad(Car):
    '''
    - внедорожник:    ................off-road vehicle
    1. рамный или нет ................framed
    2. полный привод  ................all_wheel_drive
    3. блокировка     ................blocking
    '''

    def __init__(self,
                 type_car : str = 'Внедорожник',
                 framed=False,
                 all_wheel_drive=False,
                 blocking=False):

        super().__init__( name="",price=0, color="", power=0)
        self.type_car = type_car
        self.framed = framed
        self.all_wheel_drive = all_wheel_drive
        self.blocking = blocking

    def typ_car(self):
        return self.type_car

    # Рама усилена или нет : bool
    def swich_fram(self):
        '''
        Опция: нет -> False
               есть -> True
        '''
        # add_framed = self.toggle_attribute(self, 'framed')
        # return add_framed
        self.framed = not self.framed

    # Полный привод : bool
    def all_drive(self):
        '''
        Опция: нет -> False
               есть -> True
        '''
        # add_all_drive = self.toggle_attribute(self, 'all_wheel_drive')
        # return add_all_drive
        self.all_wheel_drive = not self.all_wheel_drive

    # блокировка : bool
    def switch_blockinging(self):
        '''
        Опция: нет -> False
               есть -> True
        '''
        # add_blockinging = self.toggle_attribute(self, 'blocking')
        # return add_blockinging
        self.blocking = not self.blocking

    def __str__(self):
        return (f"\nАвто {self.type_car}: {self.name}\n"
                f"===============================\n"
                f"Рамная конструкция : "
                f"{'Стандарт' if not self.framed else 'Усилена'}\n"
                f"Полный привод .... : "
                f"{'+' if not self.all_wheel_drive else '-'}\n"
                f"Блокировка ....... : "
                f"{'+' if not self.blocking else '-'}")

    def __del__(self):
        pass


class Cargo(Car):
    '''
    - грузовой .......................cargo
    1. тоннаж  .......................tonnage
    2. возможность установки прицепа .installing_trailer
    3. наличие спального места .......sleeping_place
    4. кол-во мест             .......number_seats
    '''

    def __init__(self,
                 type_car : str = 'грузовой',
                 tonnage : float = 3.5,
                 installing_trailer : bool = False,
                 sleeping_place : bool = False,
                 number_seats : int = 2):
        super().__init__(name="", price=0, color="", power=0)
        self.type_car = type_car
        self.tonnage = tonnage
        self.installing_trailer = installing_trailer
        self.sleeping_place = sleeping_place
        self.number_seats = number_seats

    # Возможность установки прицепа
    def install_trailer(self):
        '''
        Опция: нет -> False
               есть -> True
        '''
        self.installing_trailer = not self.installing_trailer

    # Выбор кол-ва мест для сна
    def sleep_place(self):
        '''
        Опция: 1 место -> False
               2 места -> True
        '''
        selected_places = Logic.quantity()

        confirm = input("Подтвердить опцию:\n"
                        "-> Пробел : Отказаться\n"
                        "-> Ввод   : Подтвердить\n")
        if confirm != "":
            selected_places = None

        if selected_places is None:
            self.sleeping_place = False
        else:
            self.sleeping_place = (selected_places == 2)

        return selected_places


    # количество мест
    def set_number_seats(self):
        '''
        Опция: прибавляется через счетчик class Logic
        '''
        seats_count = Logic.counter()  # Используем счётчик для количества мест
        self.number_seats = seats_count
        return seats_count


def main():
    name = input()
    o_Sedan = Sedan.name(name)
    print(o_Sedan)
    o_OffRoad = OffRoad()
    print(o_OffRoad)


if __name__ == "__main__":
    main()

