class Car:
    logo = "Lada"
    indastry = "Автопром"

    def __init__(self,
                 model='',
                 release=0,
                 manufacturer='',
                 engineV=0.0, color='',
                 price=0):
        self.model = model
        self.release = release
        self.manufacturer = manufacturer
        self.engineV = engineV
        self.color = color
        self.price = price

    def user_choice(self):
        print("Завод: ", Car.logo)
        self.model = input("Введите модель автомобиля: ")
        try:
            self.release = int(input("Введите год выпуска: "))
        except ValueError:
            print("Ошибка! Год выпуска должен быть числом.")
            exit()
        self.manufacturer = input("Введите производителя: ")
        try:
            self.engineV = float(input("Введите объем двигателя (в литрах): "))
        except ValueError:
            print("Ошибка! Объем двигателя должен быть числом с точкой.")
            exit()
        self.color = input("Введите цвет автомобиля: ")
        try:
            self.price = int(input("Введите стоимость автомобиля: "))
        except ValueError:
            print("Ошибка! Стоимость должна быть целым числом.")
            exit()

    # Единственный метод вывода, работающий по принципу перегрузки
    def output_data(self, mode=''):

        a_print = f"====={Car.indastry:^16}==================="

        if mode.lower() == '1':  # Режим сокращения
            print(a_print)
            print(f"Марка: {self.model}, Год выпуска: {self.release}")
            print("=" * len(a_print))
        else:
            print(a_print)
            print(f"Модель          : {self.model}")
            print(f"Год выпуска     : {self.release}")
            print(f"Производитель   : {self.manufacturer}")
            print(f"Объем двигателя : {self.engineV:.1f} л")
            print(f"Цвет            : {self.color}")
            print(f"Цена            : {self.price:,d} руб.")
            print("=" * len(a_print))

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


def menu_logic():
    car = Car()
    car.user_choice()
    while True:
        print("----------------------------")
        print("Какой формат вывода выбрать:")
        print("1     : Сокращённый отчет")
        print("2     : Полный отчет")
        print("Enter : Выход")
        print("----------------------------")
        format_choice = input().strip().lower()
        if format_choice == '':
            break
        else:
            car.output_data(format_choice)

# Тестируем класс
if __name__ == "__main__":
    menu_logic()