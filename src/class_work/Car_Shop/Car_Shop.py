'''
На завод по производству автомобилей необходимо создать
систему классов для ведения базы данныхвсех выпущенных авто.
Все автомобили обладают необходимыми характеристиками:

1 цена -     .....................price
2 название - .....................name
3 цвет -     .....................color
4 мощность - .....................power

Необходимо реализовать классы для следующих видов машин:

- седан:   .......................sedan
1.  АКПП - .......................auto_transmission
    МКПП - .......................manual_transmission
2. кол-во дополнительных опций - additional_options

- внедорожник:    ................off-road vehicle
1. рамный или нет ................framed
2. полный привод  ................all_wheel_drive
3. блокировка     ................blocking

- грузовой
1. тоннаж
2. возможность установки прицепа .installing_trailer
3. наличие спального места .......sleeping place
4. кол-во мест             .......number_seats
'''


class Logic:
    @staticmethod
    def toggle_attribute(obj, attr_name):
        current_value = getattr(obj, attr_name)
        new_value = not current_value
        setattr(obj, attr_name, new_value)
        return new_value


class Car(Logic):
    def __init__(self, name: str = "", price: int = 0, color: str = "",
                 power: int = ""):
        self.name = name
        self.price = price
        self.color = color
        self.power = power

    def name_car(self):
        return self.name

    def price_car(self):
        return self.price

    def color_car(self):
        return self.color

    def power_car(self):
        return self.power

    def __str__(self):
        return (f"Автомобиль: {self.name} : {self.price} рублей."
                 f"\nМощность: {self.power}\nЦвет: {self.color}")

    def __dell__(self):
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

        super().__init__(price=0, name="", color="", power=0)
        self.auto_transmission = auto_transmission
        self.additional_options = additional_options

    # Выбирает опцию МККП/АККП
    def transmission(self):
        option_transmission = self.toggle_attribute(self, 'auto_transmission')
        return option_transmission

    # Выбырает доп_опции: есть/нет
    def add_option(self):
        add_options = self.toggle_attribute(self, 'additional_options')
        return add_options

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
                 framed=False,
                 all_wheel_drive=False,
                 blocking=False):
        super().__init__(price=0, name="", color="", power=0)
        self.framed = framed
        self.all_wheel_drive = all_wheel_drive
        self.blocking = blocking

    def choice_framed(self):
        if self.framed == False:
            self.framed = True
            return f"рама усиленная"
        else:
            self.framed = False
            return f"рама не усиленная"

    def all_drive(self):
        if self.all_wheel_drive == False:
            self.all_wheel_drive = True
            return f"полный привод"
        else:
            self.all_wheel_drive = False
            return f"--"

    def blockinging(self):
        if self.blocking == False:
            self.blocking = True
            return f"+ ABS +"
        else:
            self.blocking = False
            return f"- --- -"


class Cargo(Car):
    '''
    - грузовой .......................cargo
    1. тоннаж  .......................tonnage
    2. возможность установки прицепа .installing_trailer
    3. наличие спального места .......sleeping place
    4. кол-во мест             .......number_seats
    '''


def main():
    o_Sedan = Sedan()
    print(o_Sedan)


if __name__ == "__main__":
    main()
