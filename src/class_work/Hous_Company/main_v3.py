'''
Хорошо, давай реализуем нашу программу с использованием абстрактных
классов и интерфейсов. Такое решение даст нам большую гибкость в будущем
и позволит легко добавлять новые типы компонентов.

### Шаги:
1. Определим абстракцию с помощью абстрактных классов (`ABC`).
2. Используем наследование для создания конкретных классов
    (подвал, этаж, крыша и пр.).
3. Сделаем интерфейс (класс-обертку), который позволит пользователю
    конфигурировать дом.

### Реализация:
'''
import abc
from abc import ABC, abstractmethod

# 1. Абстрактный класс Component для компонентов дома
class Component(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass

# 2. Абстрактный класс BuildingElement для элементов дома
class BuildingElement(Component):
    def __init__(self,
                 area=0.0):
        self.area = area

    def calculate_cost(self):
        return self.area * 5000  # базовая ставка стоимости квадратного метра

# 3. Конкретные классы компонентов дома
class Basement(BuildingElement):
    def __init__(self,
                 area=0.0,
                 foundation_type=None,
                 communications=False,
                 electricity=220):
        super().__init__(area)
        self.foundation_type = foundation_type
        self.communications = communications
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.communications:
            cost += 10000  # дополнительно за коммуникации
        return cost

class Floor(BuildingElement):
    def __init__(self,
                 area=0.0,
                 rooms=1,
                 bathrooms=1,
                 electricity=220):
        super().__init__(area)
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += self.rooms * 10000  # дополнительно за каждую комнату
        cost += self.bathrooms * 15000  # дополнительно за каждый санузел
        return cost

class Roof(BuildingElement):
    def __init__(self,
                 area=0.0,
                 attic=False,
                 roof_type=None,
                 satellite_dish=False,
                 electricity=220):
        super().__init__(area)
        self.attic = attic
        self.roof_type = roof_type
        self.satellite_dish = satellite_dish
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.attic:
            cost += 10000  # дополнительно за чердак
        if self.satellite_dish:
            cost += 5000  # дополнительно за спутниковую антенну
        return cost

class AdditionalBuilding(BuildingElement):
    def __init__(self,
                 area=0.0,
                 building_types=[]):
        super().__init__(area)
        self.building_types = building_types

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += len(self.building_types) * 10000  # дополнительно за каждую постройку
        return cost

# 4. Основной класс House для объединения всех компонентов
class House:
    def __init__(self,
                 basement=None,
                 floors=[],
                 roof=None,
                 additional_buildings=None):
        self.basement = basement
        self.floors = floors
        self.roof = roof
        self.additional_buildings = additional_buildings

    def calculate_total_cost(self):
        total_cost = 0
        if self.basement:
            total_cost += self.basement.calculate_cost()
        for floor in self.floors:
            total_cost += floor.calculate_cost()
        if self.roof:
            total_cost += self.roof.calculate_cost()
        if self.additional_buildings:
            total_cost += self.additional_buildings.calculate_cost()
        return total_cost

# 5. Интерфейс для пользователя
def create_house():
    print("Настройте Ваш дом:")

    # Подвал
    basement_area = float(input("Площадь подвала (кв.м): "))
    foundation_type = input("Тип фундамента (ленточный/свайный): ")
    communications = input("Коммуникации (да/нет)? ") == "да"
    basement = Basement(area=basement_area,
                        foundation_type=foundation_type,
                        communications=communications)

    # Этажи
    floors_count = int(input("Сколько этажей хотите построить? "))
    floors = []
    for i in range(floors_count):
        floor_area = float(input(f"Площадь этажа {i+1} (кв.м): "))
        rooms = int(input(f"Количество комнат на этаже {i+1}: "))
        bathrooms = int(input(f"Количество санузлов на этаже {i+1}: "))
        floors.append(Floor(area=floor_area,
                            rooms=rooms,
                            bathrooms=bathrooms))

    # Крыша
    roof_area = float(input("Площадь крыши (кв.м): "))
    attic = input("Чердак (да/нет)? ") == "да"
    roof_type = input("Тип крыши (односкатная/двускатная): ")
    satellite_dish = input("Спутниковая антенна (да/нет)? ") == "да"
    roof = Roof(area=roof_area,
                attic=attic,
                roof_type=roof_type,
                satellite_dish=satellite_dish)

    # Дополнительные постройки
    additional_area = float(input("Площадь дополнительных построек (кв.м): "))
    additional_types = input("Какие дополнительные постройки будете строить "
                             "(перечислите через пробел): ").split()
    additional_buildings = AdditionalBuilding(area=additional_area,
                                              building_types=additional_types)

    # Создаем объект Дома
    house = House(basement=basement,
                  floors=floors,
                  roof=roof,
                  additional_buildings=additional_buildings)
    return house

# Основная функция
def main():
    house = create_house()
    total_cost = house.calculate_total_cost()
    print(f"\nОбщая стоимость дома: {total_cost:,.2f} руб.")

if __name__ == "__main__":
    main()
'''

### Что мы сделали:
- Создали абстрактный класс `Component`, от которого наследуются все 
    строительные элементы.
- Разработали специализированные классы для подвала, этажей, крыши и 
    дополнительных построек.
- Реализовали интерфейс через консоль, позволяющий пользователю 
    настроить параметры дома и увидеть итоговую стоимость.

### Демонстрация работы программы:
Настройте Ваш дом:
Площадь подвала (кв.м): 100
Тип фундамента (ленточный/свайный): ленточный
Коммуникации (да/нет)? да
Сколько этажей хотите построить? 2
Площадь этажа 1 (кв.м): 150
Количество комнат на этаже 1: 3
Количество санузлов на этаже 1: 2
Площадь этажа 2 (кв.м): 120
Количество комнат на этаже 2: 2
Количество санузлов на этаже 2: 1
Площадь крыши (кв.м): 200
Чердак (да/нет)? да
Тип крыши (односкатная/двускатная): двускатная
Спутниковая антенна (да/нет)? да
Площадь дополнительных построек (кв.м): 50
Какие дополнительные постройки будете строить (перечислите через пробел): баня гараж
Общая стоимость дома: 1,855,000.00 руб.

### Преимущества нашего подхода:
- **Абстракция**: единая концепция для всех компонентов дома.
- **Расширяемость**: легко добавить новые типы компонентов или изменить 
        существующие.
- **Интерфейс**: удобный текстовый интерфейс для быстрой настройки дома.

Если возникают вопросы или нужно что-то изменить, дай мне знать!
'''