from abc import ABC, abstractmethod

class CostBuild(ABC):
    '''Базовый абстрактный класс для рассчета строительных затрат'''
    def __init__(self,
                 base_cost_per_meter=5000.0):
        self.base_cost_per_meter = base_cost_per_meter

    @abstractmethod
    def calculate_total_cost(self):
        pass

class Basement(CostBuild):
    '''Подвал'''

    def __init__(self,
                 area=0.0,
                 foundation_type="",
                 communication=False,
                 electric_power=220):
        super().__init__()
        self.area = area
        self.foundation_type = foundation_type
        self.communication = communication
        self.electric_power = electric_power

    def calculate_total_cost(self):
        total_cost = self.area * self.base_cost_per_meter
        if self.communication:
            total_cost *= 1.1    # +10% коммуникации
        return total_cost

class Floor(CostBuild):
    '''Этаж'''
    def __init__(self,
                 area=0.0,
                 num_rooms=1,
                 num_bathrooms=1,
                 electric_power=220):
        self.area = area
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.electric_power = electric_power

    def calculate_total_cost(self):
        room_factor = self.num_rooms * 1000 # стоимость постройки комнат
        bathroom_factor = self.num_bathrooms * 1500 # санузел
        total_cost = (self.area * self.base_cost_per_meter + room_factor +
                      bathroom_factor)
        return total_cost

class Roof(CostBuild):
    '''Крыша'''
    def __init__(self,
                 roof_area=0.0,
                 has_attic=False,
                 roof_type="",
                 satellite_dish=False,
                 electric_power=220):
        super().__init__()
        self.roof_area = roof_area
        self.has_attic = has_attic
        self.roof_type = roof_type
        self.satellite_dish = satellite_dish
        self.electric_power = electric_power

    def calculate_total_cost(self):
        total_cost = self.roof_area * self.base_cost_per_meter
        if self.has_attic:
            total_cost *= 1.1 # +10% чердак
        if self.satellite_dish:
            total_cost += 5000 # спутниковая тарелка
        return total_cost

class AdditionalBuilding(CostBuild):
    '''Дополнительные постройки'''
    def __init__(self,
                 building_area=0.0,
                 types=['гараж'],
                 electric_power=220):
        super().__init__()
        self.building_area = building_area
        self.types = types
        self.electric_power = electric_power

    def calculate_total_cost(self):
        total_cost = self.building_area * self.base_cost_per_meter
        additional_cost = len(self.types) * 10000 # доп опции +10 000
        return total_cost + additional_cost


class HomeConfigurator:
    def __init__(self, house_components, price_manager):
        self.house_components = house_components
        self.price_manager = price_manager

    def calculate_total_cost(self):
        total_cost = 0
        # Сюда помещается логика расчета стоимости на основании
        # предоставленных компонентов и прайс-менеджера

        # Пример простого расчета:
        for key, values in self.house_components.items():
            if key == "Подвал":
                total_cost += values["area"] * self.price_manager.get_price(
                    "подвал")
            elif key.startswith("Этаж"):
                total_cost += values["area"] * self.price_manager.get_price(
                    "этаж")
                total_cost += values[
                                  "num_rooms"] * self.price_manager.get_price(
                    "комната")
                total_cost += values[
                                  "num_bathrooms"] * self.price_manager.get_price(
                    "санузел")
            elif key == "Крыша":
                total_cost += values["square"] * self.price_manager.get_price(
                    "крыша")
                if values["satellite_dish"]:
                    total_cost += self.price_manager.get_price("антенна")
            elif key == "Доп. постройки":
                for building_type in values["types"]:
                    total_cost += self.price_manager.get_price(building_type)

        return total_cost

'''
Строительная компания
Смета                  - Estimate
Итоговая проекта

==============
Создать класс:
- позволяет по желанию клиента конфигурировать объект Дом, 
внутри которого будут находиться поля объекта приведенных выше классов

Классы:
1. Подвал:
 пл  Площадь
 пл  тип фундамента
 опц Подводимые коммуникации
 опц мощность входной электрики  
 
2. Этаж
 пл  Площадь
 +%  кол-во комнат
 +%  кол-во санузлов
 опц мощность входной электрики

3. Крыша
 опц  наличие чердака  - attic
 пл   площадь чердака  - square   
 +%   тип крыши        - type_roof
 опц  спутниковая тарелка - satellite_dish
 опц  мощность входной электрики - electrics

4. доп-постройки на территории
 пл  площадь
 +%  виды построек + 10%
 опц мощность входной электрики
 
5. опц   доп-опции
=====================
начнем с папки:

project_root/
├── src/
│   ├── core/
│   │   ├── costbuild.py        # Основные классы и механизмы расчета стоимости
│   │   ├── homeconfigurator.py # Менеджмент настроек дома
│   │   └── pricelistmanager.py # Менеджмент прайс-листов
│   ├── ui/
│   │   ├── menus.py            # Реализация меню
│   │   └── interface.py        # Основной интерфейс взаимодействия
│   └── __init__.py             # Пустой файл для преобразования каталога в пакет
├── prices.json                 # Хранение текущих цен
└── run.py                      # Главная точка входа в программу
'''
