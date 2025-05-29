class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, passengers):
        self.current_passengers += passengers
        return self

    def __sub__(self, passengers):
        self.current_passengers -= passengers
        return self

    def __iadd__(self, passengers):
        self.current_passengers += passengers
        return self

    def __isub__(self, passengers):
        self.current_passengers -= passengers
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"Самолёт {self.model}: {self.current_passengers}/{self.max_passengers} пассажиров"


# Создаём два самолёта
plane1 = Airplane(model="Boeing 747", max_passengers=400, current_passengers=200)
plane2 = Airplane(model="Airbus A320", max_passengers=180, current_passengers=100)

print(plane1)
print(plane2)

# Проверка на равенство типов
print(plane1 == plane2)  # False, так как модели разные

# Добавляем пассажиров
plane1 += 50
print(plane1.current_passengers)  # 250
print(plane1)

# Удаляем пассажиров
plane2 -= 30
print(plane2.current_passengers)  # 70
print(plane2)

# Сравнение по максимальной вместимости
print(plane1 > plane2)  # True, Boeing вмещает больше пассажиров
print(plane1 <= plane2)  # False, Boeing вмещает больше пассажиров