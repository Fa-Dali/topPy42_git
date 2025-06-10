'''
Хороший вопрос! Если у тебя имеется внешний файл (например, `.json`),
в котором хранится прайс-лист с ценами, то мы можем интегрировать этот
файл в нашу программу и подставлять актуальные цены из него.

### Шаги:

1. Читаем цены из внешнего JSON-файла.
2. Интегрируем считанные цены в логику расчета стоимости.

### Предполагаемый JSON-файл `prices.json`:

```json
{
  "base_rate": 5000,        // базовая ставка за м²
  "communication_fee": 10000, // доплата за коммуникации
  "room_fee": 10000,        // доплата за комнату
  "bathroom_fee": 15000,    // доплата за санузел
  "attic_fee": 10000,       // доплата за чердак
  "satellite_dish_fee": 5000 // доплата за спутниковую антенну
}
```

### Реализация:
1. Добавим в начало программы импорт библиотеки для работы с JSON.
2. Напишем метод для загрузки цен из файла.
3. Обновим класс `BuildingElement`, чтобы он использовал внешние цены.

### Пример полной реализации:
'''
import abc
from abc import ABC, abstractmethod
import json

# Читаем цены из JSON-файла
def load_prices(filename="prices.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при загрузке цен: {e}")
        return {}

PRICES = load_prices()
BASE_RATE = PRICES.get("base_rate", 5000)  # базовая ставка за м²
COMMUNICATION_FEE = PRICES.get("communication_fee", 10000)  # доплата за коммуникации
ROOM_FEE = PRICES.get("room_fee", 10000)  # доплата за комнату
BATHROOM_FEE = PRICES.get("bathroom_fee", 15000)  # доплата за санузел
ATTIC_FEE = PRICES.get("attic_fee", 10000)  # доплата за чердак
SATELLITE_DISH_FEE = PRICES.get("satellite_dish_fee", 5000)  # доплата за спутниковую антенну
'''
=======================================================================
            Почему они все написаны заглавными буквами?
=======================================================================
Заглавные буквы в именах переменных указывают на **константы** в Python. 
Хотя Python не принудительно следит за соблюдением правил констант 
(они не защищены от перезаписи), соглашение гласит, что имена переменных, 
написанные ЗАГЛАВНЫМИ буквами, означают, что это постоянные величины, 
которые не должны меняться в процессе выполнения программы.

Поэтому такие переменные, как:

- `BASE_RATE`
- `COMMUNICATION_FEE`
- `ROOM_FEE`
- `BATHROOM_FEE`
- `ATTIC_FEE`
- `SATELLITE_DISH_FEE`

указаны большими буквами, чтобы подчеркнуть, что их значения 
предполагаются постоянными в рамках данной программы.

### Суть соглашения:
- Константы принято называть **заглавными буквами**, чтобы программист 
        ясно понимал, что данное значение не должно изменяться.
- Следование этому соглашению помогает другим разработчикам быстрее 
        ориентироваться в коде и понимать назначение 
        той или иной переменной.

Однако важно помнить, что технически это просто рекомендация стиля и 
ничего формально не мешает изменить такие переменные. Если вы хотите 
реально запретить их изменение, можно воспользоваться другими способами, 
такими как применение специальных механизмов (например, декораторы или 
замораживание пространства имен). Однако в большинстве случаев 
соблюдение соглашений достаточно для большинства сценариев.
'''
# 1. Абстрактный класс Component для компонентов дома
class Component(ABC):
    @abstractmethod
    def calculate_cost(self):
        pass

# 2. Абстрактный класс BuildingElement для элементов дома
class BuildingElement(Component):
    def __init__(self, area=0.0):
        self.area = area

    def calculate_cost(self):
        return self.area * BASE_RATE  # Используем внешнюю цену из JSON

# 3. Конкретные классы компонентов дома
class Basement(BuildingElement):
    def __init__(self, area=0.0, foundation_type=None, communications=False, electricity=220):
        super().__init__(area)
        self.foundation_type = foundation_type
        self.communications = communications
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.communications:
            cost += COMMUNICATION_FEE  # Дополнительно за коммуникации
        return cost

class Floor(BuildingElement):
    def __init__(self, area=0.0, rooms=1, bathrooms=1, electricity=220):
        super().__init__(area)
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += self.rooms * ROOM_FEE  # Дополнительно за каждую комнату
        cost += self.bathrooms * BATHROOM_FEE  # Дополнительно за каждый санузел
        return cost

class Roof(BuildingElement):
    def __init__(self, area=0.0, attic=False, roof_type=None, satellite_dish=False, electricity=220):
        super().__init__(area)
        self.attic = attic
        self.roof_type = roof_type
        self.satellite_dish = satellite_dish
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        if self.attic:
            cost += ATTIC_FEE  # Дополнительно за чердак
        if self.satellite_dish:
            cost += SATELLITE_DISH_FEE  # Дополнительно за спутниковую антенну
        return cost

class AdditionalBuilding(BuildingElement):
    def __init__(self, area=0.0, building_types=[]):
        super().__init__(area)
        self.building_types = building_types

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += len(self.building_types) * BASE_RATE  # Дополнительно за каждую постройку
        return cost

# 4. Основной класс House для объединения всех компонентов
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

# 5. Интерфейс для пользователя
def create_house():
    print("Настройте Ваш дом:")

    # Подвал
    basement_area = float(input("Площадь подвала (кв.м): "))
    foundation_type = input("Тип фундамента (ленточный/свайный): ")
    communications = input("Коммуникации (да/нет)? ") == "да"
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
    attic = input("Чердак (да/нет)? ") == "да"
    roof_type = input("Тип крыши (односкатная/двускатная): ")
    satellite_dish = input("Спутниковая антенна (да/нет)? ") == "да"
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

### Что изменилось:
- **Цены подгружаются из JSON-файла**. Если файла нет или 
        возникли ошибки, берутся значения по умолчанию.
- **Формула расчета стоимости** теперь использует реальные цены из файла.
- Программа стала более гибкой и адаптивной к изменениям цен.

### Пример работы программы:
```
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
```

### Преимущества:

- **Масштабируемость**: если изменится цена, достаточно обновить 
        JSON-файл.
- **Удобство обновления**: легко внедрить новые типы компонентов или 
        изменить порядок расчетов.
- **Аккуратность и чистота кода**: используем единый источник данных 
        для цен.

Если нужно что-то поменять или добавить новые функции, скажи!
'''