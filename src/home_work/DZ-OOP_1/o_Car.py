class Car:
    def __init__(self,
                 model = '',
                 release = 0,
                 manufacturer='',
                 engineV=0.0,
                 color='',
                 price=0):

        self.model        = model
        self.realise      = release
        self.manufacturer = manufacturer
        self.engineV      = engineV
        self.color        = color
        self.price        = price

    def user_choice(self):
        self.model        = input("введите модель автомобиля: ")
        self.realise      = input("введите год выпуска: ")
        self.manufacturer = input("введите производителя: ")
        self.engineV      = input("введите объём двигателя (в литрах): ")
        self.color        = input("введите цвет автомобиля: ")
        self.price        = int(input("введите стоимость автомобиля: "))

    def output_data(self):
        print(f"=================================")
        print(f"Модель          : {self.model}")
        print(f"Год выпуска     : {self.realise}")
        print(f"Производитель   : {self.manufacturer}")
        print(f"Объём двигателя : {self.engineV}")
        print(f"Цвет            : {self.color}")
        print(f"Цена            : {self.price} рублей")
        print(f"=================================")

    def get_model(self):
        return self.model

    def get_realise(self):
        return self.realise

    def get_manufacturer(self):
        return self.manufacturer

    def get_engineV(self):
        return self.engineV

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

if __name__ == "__main__":
    car = Car()
    car.user_choice()
    car.output_data()