class Stadium:
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
        self.name_stadium  = input("введите название стадиона    : ")
        self.date_opening  = input("введите год открытия         : ")
        self.country       = input("введите страну               : ")
        self.city          = input("введите город                : ")
        self.capacity      = input("введите вместимость стадиона : ")

    def output_data(self):
        print(f"=================================")
        print(f"Стадион      : {self.name_stadium}")
        print(f"Год открытия : {self.date_opening} г.")
        print(f"Страна       : {self.country}")
        print(f"Город        : {self.city}")
        print(f"Вместимость  : {self.capacity}")
        print(f"=================================")

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

if __name__ == "__main__":
    stadium = Stadium()
    stadium.user_choice()
    stadium.output_data()