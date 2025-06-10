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

    def __int__(self):
        return int(self.square()) # округлелие площади вниз до целого числа

    def __str__(self):
        raise NotImplementedError("Метод строкового представления "
                                  "должен быть реализован в производных "
                                  "классах")

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

    def __str__(self):
        return (f"\nПрямоугольник\n"
                f"  длина  : {self.length}{unit}\n"
                f"  ширина : {self.width}{unit}\n"
                f"---------------\n"
                f"Площадь  : {self.square():.2f}{unit}^2")

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

    def __str__(self):
        return (f"\nКруг\n"
                f"  радиус : {self.radius}{unit}\n"
                f"---------------\n"
                f"Площадь  : {self.square():.2f}{unit}^2")

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

    def __str__(self):
        return (f"\nПрямоугольный треугольник\n"
                f"  катет 1 : {self.catheter_1}{unit}\n"
                f"  катет 2 : {self.catheter_2}{unit}\n"
                f"---------------\n"
                f"Площадь  : {self.square():.2f}{unit}^2")

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

    def __str__(self):
        return (f"\nТрапеция с основанием\n"
                f"  основание 1 : {self.footing_1}{unit}\n"
                f"  основание 2 : {self.footing_2}{unit}\n"
                f"  высота      : {self.height}{unit}\n"
                f"---------------\n"
                f"Площадь  : {self.square():.2f}{unit}^2")


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

# Определяем объекты
o_Rectangle = Rectangle(5, 10)
o_Circle = Circle(7)
o_RightAngledTriangle =RightAngledTriangle(3, 4)
o_Trapezoid = Trapezoid(5, 10, 6)

# Вывод результата
print(f"Площадь прямоугольника : {o_Rectangle.square()} ({unit})")
print(f"Площадь круга          : {o_Circle.square():.2f} ({unit})")
print(f"Площадь треугольника   : {o_RightAngledTriangle.square()} "
      f"({unit})")
print(f"Площадь трапеции       : {o_Trapezoid.square()} ({unit})")
print()
print("Магический метод __int__:", int(o_Rectangle))
print("Магический метод __str__:", str(o_Circle))

