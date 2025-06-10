'''
Создайте базовый класс Shape для рисования плоскихфигур.
Определить методы:
■ Show() — вывод на экран информации о фигуре;
■ Save() — сохранение фигуры в файл;
■ Load() — считывание фигуры из файла.

Определить производные классы:
■ Square — квадрат, который характеризуется координатами
            левого верхнего угла и длиной стороны;
■ Rectangle — прямоугольник с заданными координатами верхнего левого
            угла и размерами;
■ Circle — окружность с заданными координатами центра и радиусом;
■ Ellipse — эллипс с заданными координатами верхнегоугла описанного
            вокруг него прямоугольника со сторонами, параллельными
            осям координат, и размерамиэтого прямоугольника.

Создайте список фигур, сохраните фигуры в файл,загрузите в другой список
и отобразите информацию окаждой из фигур.
'''

from abc import ABC, abstractmethod
import json

# Базовый абстрактный класс Shape
class Shape(ABC):
    @abstractmethod
    def Show(self):
        pass

    @abstractmethod
    def Save(self, filename):
        pass

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        # Анализируем тип фигуры, указанный в файле
        figure_type = data.get("type")
        if figure_type == "square":
            return Square(data["x"], data["y"], data["side_length"])
        elif figure_type == "rectangle":
            return Rectangle(data["x"], data["y"], data["width"],
                             data["height"])
        elif figure_type == "circle":
            return Circle(data["center_x"], data["center_y"], data["radius"])
        elif figure_type == "ellipse":
            return Ellipse(data["top_left_x"], data["top_left_y"],
                           data["width"], data["height"])
        else:
            raise ValueError(f"Неизвестный тип фигуры: {figure_type}")


# Класс Square (Квадрат)
class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def Show(self):
        print(f"Квадрат\n"
              f"с левым верхним углом ({self.x}, {self.y})\n"
              f"и стороной {self.side_length}\n"
              f"======================")

    def Save(self, filename):
        data = {
            "type": "square",
            "x": self.x,
            "y": self.y,
            "side_length": self.side_length
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data["x"], data["y"], data["side_length"])


# Класс Rectangle (Прямоугольник)
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Прямоугольник\n"
              f"с левым верхним углом ({self.x}, {self.y}),\n"
              f"шириной {self.width} и\n"
              f"высотой {self.height}\n"
              f"======================")

    def Save(self, filename):
        data = {
            "type": "rectangle",
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data["x"], data["y"], data["width"], data["height"])


# Класс Circle (Окружность)
class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def Show(self):
        print(f"Окружность\n"
              f"с центром ({self.center_x}, {self.center_y}) и\n"
              f"радиусом {self.radius}\n"
              f"======================")

    def Save(self, filename):
        data = {
            "type": "circle",
            "center_x": self.center_x,
            "center_y": self.center_y,
            "radius": self.radius
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data["center_x"], data["center_y"], data["radius"])


# Класс Ellipse (Эллипс)
class Ellipse(Shape):
    def __init__(self, top_left_x, top_left_y, width, height):
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Эллипс\n"
              f"с верхним левым углом ({self.top_left_x}, {self.top_left_y}),\n"
              f"шириной {self.width} и\n"
              f"высотой {self.height}\n"
              f"======================")

    def Save(self, filename):
        data = {
            "type": "ellipse",
            "top_left_x": self.top_left_x,
            "top_left_y": self.top_left_y,
            "width": self.width,
            "height": self.height
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return cls(data["top_left_x"], data["top_left_y"], data["width"], data["height"])


# Пример использования
if __name__ == "__main__":
    # Создаем список фигур
    shapes_list = [
        Square(10, 10, 5),
        Rectangle(20, 20, 30, 40),
        Circle(50, 50, 15),
        Ellipse(60, 60, 20, 30)
    ]

    # Выводим информацию о созданных фигурах
    print("**********************")
    print("   Исходные фигуры:")
    print("**********************")
    for shape in shapes_list:
        shape.Show()

    # Сохраняем каждую фигуру в файл
    for idx, shape in enumerate(shapes_list):
        shape.Save(f"shape{idx + 1}.json")

    # Читаем фигуры из файлов и записываем в новый список
    loaded_shapes = []
    for idx in range(len(shapes_list)):
        loaded_shape = Shape.Load(f"shape{idx + 1}.json")
        loaded_shapes.append(loaded_shape)

    # Выводим информацию о прочитанных фигурах
    print("\n**********************")
    print("  Загруженные фигуры:")
    print("**********************")
    for shape in loaded_shapes:
        shape.Show()

