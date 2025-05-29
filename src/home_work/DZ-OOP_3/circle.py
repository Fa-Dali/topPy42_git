import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    # изменение радиуса
    def __add__(self, delta):
        return Circle(self.radius + delta)

    def __sub__(self, delta):
        return Circle(self.radius - delta)

    def __iadd__(self, delta):
        self.radius += delta
        return self

    def __isub__(self, delta):
        self.radius -= delta
        return self

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return (f"Круг с радиусом {self.radius:.2f}, "
                f"длина окружности: {self.circumference():.2f}")

circle1 = Circle(5)
circle2 = Circle(10)

# Проверка на равенство радиусов
print(circle1 == circle2)  # False

# Сравнение длин окружностей
print(circle1 < circle2)  # True
print(circle1 >= circle2)  # False

# Увеличение радиуса
circle1 += 3
print(circle1)  # Круг с радиусом 8.00, длина окружности: 50.27
# Уменьшение радиуса
circle1 -= 2
print(circle1)  # Круг с радиусом 6.00, длина окружности: 37.70