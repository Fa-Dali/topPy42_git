class BaseComponent:
    def __init__(self, area=0.0):
        self.area = area

    def calculate_cost(self):
        # Базовая стоимость равна площади х базовую ставку ($5000/м²)
        return self.area * 5000

class Basement(BaseComponent):
    def __init__(self, area=0.0, foundation_type=None, communications=False, electricity=220):
        super().__init__(area)
        self.foundation_type = foundation_type
        self.communications = communications
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.communications:
            cost += 10000  # Дополнительно за коммуникации
        return cost

class Floor(BaseComponent):
    def __init__(self, area=0.0, rooms=1, bathrooms=1, electricity=220):
        super().__init__(area)
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += self.rooms * 10000  # Дополнительно за каждую комнату
        cost += self.bathrooms * 15000  # Дополнительно за каждый санузел
        return cost

class Roof(BaseComponent):
    def __init__(self, area=0.0, attic=False, roof_type=None, satellite_dish=False, electricity=220):
        super().__init__(area)
        self.attic = attic
        self.roof_type = roof_type
        self.satellite_dish = satellite_dish
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.attic:
            cost += 10000  # Плюс стоимость чердака
        if self.satellite_dish:
            cost += 5000  # Стоимость установки спутниковой антенны
        return cost

class AdditionalBuilding(BaseComponent):
    def __init__(self, area=0.0, building_types=[]):
        super().__init__(area)
        self.building_types = building_types

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += len(self.building_types) * 10000  # Дополнительно за каждую постройку
        return cost

class House:
    def __init__(self, basement=None, floors=[], roof=None, additional_buildings=None):
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

# Функция для построения дома через интерфейс
def create_house():
    print("Конфигурируем Ваш дом:")

    # Подвал
    basement_area = float(input("Площадь подвала (кв.м): "))
    foundation_type = input("Тип фундамента (ленточный, свайный): ")
    communications = input("Подводимые коммуникации (да/нет)? ") == "да"
    basement = Basement(area=basement_area, foundation_type=foundation_type, communications=communications)

    # Этажи
    floors_count = int(input("Сколько этажей хотите построить? "))
    floors = []
    for i in range(floors_count):
        floor_area = float(input(f"Площадь этажа {i+1} (кв.м): "))
        rooms = int(input(f"Количество комнат на этаже {i+1}: "))
        bathrooms = int(input(f"Количество санузлов на этаже {i+1}: "))
        floors.append(Floor(area=floor_area, rooms=rooms, bathrooms=bathrooms))

    # Крыша
    roof_area = float(input("Площадь крыши (кв.м): "))
    attic = input("Хотите установить чердак (да/нет)? ") == "да"
    roof_type = input("Тип крыши (односкатная, двускатная): ")
    satellite_dish = input("Установить спутниковую антенну (да/нет)? ") == "да"
    roof = Roof(area=roof_area, attic=attic, roof_type=roof_type, satellite_dish=satellite_dish)

    # Дополнительные постройки
    additional_area = float(input("Площадь дополнительных построек (кв.м): "))
    additional_types = input("Какие дополнительные постройки будете строить (перечислите через пробел): ").split()
    additional_buildings = AdditionalBuilding(area=additional_area, building_types=additional_types)

    # Создаем объект Дома
    house = House(basement=basement, floors=floors, roof=roof, additional_buildings=additional_buildings)
    return house

# Основная функция
def main():
    house = create_house()
    total_cost = house.calculate_total_cost()
    print(f"\nОбщая стоимость дома: {total_cost:,.2f} руб.")

if __name__ == "__main__":
    main()

'''
Дальнейшая модернизация:
GUI: можно заменить текстовый интерфейс на графический (Tkinter, PyQt и др.).
Файловые операции: реализовать сохранение настроек дома в файл и чтение ранее созданных проектов.
Оптимизация: внести возможность гибкого ценообразования и скидок.
==================================================
Кажется, ты хотел бы посмотреть подробную схему классов и их отношений в нашей программе. Давайте посмотрим, как организованы наши классы и отношения между ними.

### Интерфейс классов (структурная схема):

1. **Основной класс: `House`**  
    Представляет сам дом, содержащий все ключевые компоненты: подвал, этажи, крышу и дополнительные постройки.

    #### Атрибуты:
    - `basement`: объект класса `Basement`
    - `floors[]`: список объектов класса `Floor`
    - `roof`: объект класса `Roof`
    - `additional_buildings`: объект класса `AdditionalBuilding`

    #### Методы:
    - `calculate_total_cost()`: вычисляет суммарную стоимость всех компонентов дома.

2. **Базовый класс: `BaseComponent`**  
    Общий предок для всех компонентов дома, устанавливает базовую логику расчета стоимости.

    #### Атрибуты:
    - `area`: площадь элемента (например, подвал, этаж, крыша).

    #### Методы:
    - `calculate_cost()`: возвращает базовую стоимость компонента.

3. **Производные классы:**

    - **`Basement`**  
        Подвал дома.

        #### Атрибуты:
        - `area`: площадь подвала.
        - `foundation_type`: тип фундамента (например, ленточный, свайный).
        - `communications`: имеются ли коммуникации (электричество, водоснабжение и т.д.).
        - `electricity`: напряжение электричества (стандартно 220V).

        #### Методы:
        - Переопределённая версия `calculate_cost()`, которая включает дополнительную плату за коммуникации.

    - **`Floor`**  
        Этаж дома.

        #### Атрибуты:
        - `area`: площадь этажа.
        - `rooms`: количество комнат.
        - `bathrooms`: количество санузлов.
        - `electricity`: напряжение электричества (стандартно 220V).

        #### Методы:
        - Переопределённая версия `calculate_cost()`, которая учитывает количество комнат и санузлов.

    - **`Roof`**  
        Крыша дома.

        #### Атрибуты:
        - `area`: площадь крыши.
        - `attic`: наличие чердака.
        - `roof_type`: тип крыши (например, односкатная, двускатная).
        - `satellite_dish`: установка спутниковой антенны.
        - `electricity`: напряжение электричества (стандартно 220V).

        #### Методы:
        - Переопределённая версия `calculate_cost()`, которая учитывает наличие чердака и спутника.

    - **`AdditionalBuilding`**  
        Дополнительные постройки (например, баня, беседка, бассейн).

        #### Атрибуты:
        - `area`: общая площадь дополнительных построек.
        - `building_types`: список типов построек (например, баня, гараж).

        #### Методы:
        - Переопределённая версия `calculate_cost()`, которая прибавляет стоимость за каждую постройку.

---

### Графическая схема классов:

```
                                +---------------+
                                |     House     |
                                +---------------+
                                    ^
                                    |
                                    |
            +-------------+---------+-----------+-------------+
            |             |         |           |             |
            v             v         v           v             v
+----------+ +---------+ +-------+ +-----------+ +--------------+
| Basement | |  Floor  | | Roof  | | Addit.Build| | BaseComponent|
+----------+ +---------+ +-------+ +-----------+ +--------------+
       |                          |                       ^
       |                          |                       |
       +----------------+---------+----------------------+
                                        (Наследование)
```

### Пример использования классов:

```python
# Создание конкретного дома
house = House(
    basement=Basement(area=100, foundation_type="ленточный", communications=True),
    floors=[
        Floor(area=150, rooms=3, bathrooms=2),
        Floor(area=120, rooms=2, bathrooms=1)
    ],
    roof=Roof(area=200, attic=True, roof_type="двухскатная", satellite_dish=True),
    additional_buildings=AdditionalBuilding(area=50, building_types=["баня", "гараж"])
)

# Получение итоговой стоимости
total_cost = house.calculate_total_cost()
print(f"Общая стоимость дома: {total_cost:,.2f} руб.")
```

---

### Преимущества дизайна:

- **Инкапсуляция**: каждый компонент ответственен за собственную стоимость и обладает собственными характеристиками.
- **Расширяемость**: легко добавить новые типы компонентов или дополнительные опции.
- **Чистая иерархия**: общая логика расчета стоимости вынесена в базовый класс, производные классы добавляют уникальные аспекты.

---

Если нужна помощь с какими-то конкретными аспектами или дальнейшей доработкой программы, сообщи!
======================================================================



'''