class Flat:
    def __init__(self, area, price):
        self.area = area  # Площадь квартиры в квадратных метрах
        self.price = price  # Цена квартиры в рублях

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return (f"Квартира площадью: {self.area} кв.м., цена: {self.price:,d} "
                f"руб.")

flat1 = Flat(area=60, price=3_500_000)
flat2 = Flat(area=70, price=4_000_000)

print(flat1)
print(flat2)
print("===============")

# Проверка равенства площадей
print(flat1 == flat2)  # False, площади разные

# Проверка неравенства площадей
print(flat1 != flat2)  # True, площади разные

# Сравнение цен
print(flat1 < flat2)   # True, первая квартира дешевле
print(flat1 >= flat2)  # False, первая квартира дешевле