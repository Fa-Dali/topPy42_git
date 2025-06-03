import  math

unit = '' # ед.измерения выбирает пользователь

# Абстрактный базовый класс
# Общий для производных классов
class Figure:
    def square(self):
        raise NotImplementedError("Метод площадь реализуется только через "
                                  "производные классы:"
                                  "\n1. Прямоугольник"
                                  "\n2. Круг"
                                  "\n3. Прямоугольный Треугольник"
                                  "\n4. Трапеция")

# Производные классы
class Rectangle(Figure):
    '''
    arg:
        :param length: длина (a)
        :param width: ширина (b)
    :return: S = a * b
    '''

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        return  self.length * self.width

class Circle(Figure):
    '''
    arg:
        :param radius: радиус (а)
    return: pi*r^2
    '''

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * (self.radius ** 2)

class RightAngledTriangle(Figure):
    '''
    arg:
        :param catheter_1: катет-1
        :param catheter_2: катет-2
    return:
        0.5 * catheter_1 * catheter_2
    '''

    def __init__(self, catheter_1, catheter_2):
        self.catheter_1 = catheter_1
        self.catheter_2 = catheter_2

    def square(self):
        return 0.5 * self.catheter_1 * self.catheter_1

class Trapezoid(Figure):
    '''
    arg:
        :param footing_1: основание_1 (а)
        :param footing_2: основание_2 (b)
        :param height: высота (h)
    return:
        ( (a + b) /2 ) * h
    '''

    def __init__(self, footing_1, footing_2, height):
        self.footing_1 = footing_1
        self.footing_2 = footing_2
        self.height = height

    def square(self):
        return ((self.footing_1 + self.footing_2) / 2) * self.height


# Определяем объекты
o_Rectangle = Rectangle(5, 10)
o_Circle = Circle(7)
o_RightAngledTriangle =RightAngledTriangle(3, 4)
o_Trapezoid = Trapezoid(5, 10, 6)

us_inp = input("Выберите единицы измерения:"
               "\n1. километры"
               "\n2. метры"
               "\n3. сантиметры"
               "\n4. миллиметры"
               "\n=============\n")

if us_inp not in ('1', '2', '3', '4'):
    print("Выбрать можно только число из перечня списка.")
else:
    if us_inp =='1':
        unit = "км"
    elif us_inp =='2':
        unit = "м"
    elif us_inp =='3':
        unit = "см"
    elif us_inp =='4':
        unit = "мм"

# Вывод результата
print(f"Площадь прямоугольника : {o_Rectangle.square()} ({unit})")
print(f"Площадь круга          : {o_Circle.square():.2f} ({unit})")
print(f"Площадь треугольника   : {o_RightAngledTriangle.square()} "
      f"({unit})")
print(f"Площадь трапеции       : {o_Trapezoid.square()} ({unit})")

