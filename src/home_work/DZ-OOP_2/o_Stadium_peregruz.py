class Stadium:
    class_building = "TV Спорт"

    def __init__(self,
                 name_stadium = '',
                 date_opening = 0,
                 country='',
                 city='',
                 capacity=''):
        self.name_stadium = name_stadium
        self.date_opening = date_opening
        self.country      = country
        self.city         = city
        self.capacity     = capacity

    def user_choice(self):
        print(f"== == == == == {Stadium.class_building:^12} == == == == ==")
        self.name_stadium  = input("введите название стадиона    : ")
        try:
            self.date_opening  = int(input("введите год открытия         : "))
        except:
            print("Ошибка! Год открытия должен быть числом.")
            exit()
        self.country       = input("введите страну               : ")
        self.city          = input("введите город                : ")
        try:
            self.capacity      = int(input("введите вместимость стадиона : "))
        except:
            print("Ошибка! Количество должно указываться числом.")
            exit()
    def output_data(self, mode=''):

        a_print = f"====={Stadium.indastry:^16}==================="

        if mode.lower() == '1': # Режим сокращенного вывода
            print(a_print)
            print(f"Город: {self.city}\nСтадион: {self.name_stadium}\n"
                  f"Вместимость: {self.capacity}")
            print("=" * len(a_print))
        else:
            print(a_print)
            print(f"== == == == == {Stadium.class_building:^12} == == == == "
                  f"==")
            print(f"=================================")
            print(f"Стадион      : {self.name_stadium}")
            print(f"Год открытия : {self.date_opening} г.")
            print(f"Страна       : {self.country}")
            print(f"Город        : {self.city}")
            print(f"Вместимость  : {self.capacity}")
            print("=" * len(a_print))

    def get_name_stadium(self):
        return self.name_stadium

    def get_date_opening(self):
        return self.date_opening

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

def menu_logic():
    stadium = Stadium()
    stadium.user_choice()
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
            stadium.output_data(format_choice)

if __name__ == "__main__":
    menu_logic()