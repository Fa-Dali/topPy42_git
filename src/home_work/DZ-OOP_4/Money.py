# Device - основной
# остальные через наследование принимают качества от родителя.
# Т.е. каждый из классов должен содержать необходимые
# для работы методы.

class Device:
    def __init__(self, description = "",loading_ingredients = False, power =
    False, motor  = False):
        self.__description = description
        self.__loading_ingredients = loading_ingredients
        self.__power = power
        self.__motor = motor
    # Описание
    # загрузка ингридиентов
    # вкл/выкл питание
    # вкл/выкл мотор
    # .
    pass

# Кофемашина
class CoffeeMashine:
    pass
# Блэндер
class Blender:
    pass

# Мясорубка
class MeatGrindef:
    pass