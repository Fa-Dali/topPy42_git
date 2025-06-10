class BaseComponent:
    def __init__(self, area=0.0):
        self.area = area

    def calculate_cost(self):
        # Базовая стоимость — площадь × базовую ставку ($5000/м²)
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
            cost += 10000  # дополнительная плата за подвод коммуникаций
        return cost

class Floor(BaseComponent):
    def __init__(self, area=0.0, rooms=1, bathrooms=1, electricity=220):
        super().__init__(area)
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.electricity = electricity

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += self.rooms * 10000  # дополнительно за каждую комнату
        cost += self.bathrooms * 15000  # дополнительно за каждый санузел
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
            cost += 10000  # плюс стоимость чердака
        if self.satellite_dish:
            cost += 5000  # стоимость установки спутниковой антенны
        return cost

class AdditionalBuilding(BaseComponent):
    def __init__(self, area=0.0, building_types=[]):
        super().__init__(area)
        self.building_types = building_types

    def calculate_cost(self):
        cost = super().calculate_cost()
        cost += len(self.building_types) * 10000  # дополнительно за каждую постройку
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

# Пример использования:
house = House(
    basement=Basement(area=100),
    floors=[
        Floor(area=150, rooms=3, bathrooms=2),
        Floor(area=120, rooms=2, bathrooms=1)
    ],
    roof=Roof(area=200, attic=True, roof_type="двухскатная"),
    additional_buildings=AdditionalBuilding(area=50, building_types=["баня", "гараж"])
)

total_cost = house.calculate_total_cost()
print(f"Общая стоимость дома: {total_cost:,.2f} руб.")