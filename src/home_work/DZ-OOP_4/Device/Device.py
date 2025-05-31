
class Device:
    def __init__(self,
                 switchIsOn = False,
                 speed : int = 0,
                 brand : str = ("Fa Dali Astro")):

        self.switchIsOn = switchIsOn
        self.speed = speed
        self.brand = brand

    def devicePower(self):
        if self.switchIsOn == False:
            self.switchIsOn = True
            self.speed = 1
            print(f"* Вкл *") ############
        elif self.switchIsOn == True:
            self.switchIsOn = False
            self.speed = 0
            print("Выкл")

    def turnOn(self):
        self.switchIsOn = True


    def turnOff(self):
        self.switchIsOn = False


    def levelUp(self):
        '''Повышение скорости, если устройство включено'''
        if not self.switchIsOn:
            print(f"{'=' * 20}")
            print("Устройство выключено.\nВключите его, чтобы регулировать "
                  "скорость.")
            print(f"{'=' * 20}")
        else:
            if self.speed < 10:
                self.speed += 1
                print(f"{'=' * 20}")
                print(f"*** скорость увеличена : {self.speed}")
                print(f"{'=' * 20}")
            else:
                print(f"{'=' * 20}")
                print("Максимальная скорость достигнута")
                print(f"{'=' * 20}")

    def levelDown(self):
        '''Понижение скорости, если устройство включено'''
        if not self.switchIsOn:
            print(f"{'=' * 20}")
            print("Устройство выключено.\nВключите его, чтобы регулировать "
                  "скорость.")
            print(f"{'=' * 20}")
        else:
            if self.speed > 10:
                self.speed -= 1
                print(f"{'=' * 20}")
                print(f"*** скорость уменьшена : {self.speed}")
                print(f"{'=' * 20}")
            else:
                print(f"{'=' * 20}")
                print("Минимальная скорость достигнута")
                print(f"{'=' * 20}")

    def show(self):
        if self.switchIsOn == False:
            print(f"{'=' * 20}\nСтатус устройства:")
            print(f"Выключен:  OFF")
            print(f"Скорость: {self.speed}\n{'=' * 20}")
        elif self.switchIsOn == True:
            print(f"{'=' * 20}\nСтатус устройства:")
            print(f"Включен : * ON *")
            print(f"Скорость: {self.speed}\n{'=' * 20}")


class CoffeeMachine(Device):
    def __init__(self,
                 description : str = "Кофе-машина : 10-скоростная",
                 switchIsOn : bool = False,
                 speed : int = 0,
                 brand: str = "Fa Dali Astro"):
        super().__init__(
            switchIsOn = switchIsOn,
            speed = speed,
            brand = brand)

        self.description = description

    # описание девайса
    def logo(self):
        return f"{self.description} : {self.brand}"

class Blender(Device):
    def __init__(self,
                 description: str = "Блендер : 10-скоростной",
                 switchIsOn: bool = False,
                 speed: int = 0,
                 brand: str = "Fa Dali Astro"):
        super().__init__(
            switchIsOn=switchIsOn,
            speed=speed,
            brand=brand)

        self.description = description

    # описание девайса
    def logo(self):
        return f"{self.description} : {self.brand}"

class MeatGrinder(Device):
    def __init__(self,
                 description: str = "Мясорубка : 10-скоростная",
                 switchIsOn: bool = False,
                 speed: int = 0,
                 brand: str = "Fa Dali Astro"):
        super().__init__(
            switchIsOn=switchIsOn,
            speed=speed,
            brand=brand)

        self.description = description

    # описание девайса
    def logo(self):
        return f"{self.description} : {self.brand}"
