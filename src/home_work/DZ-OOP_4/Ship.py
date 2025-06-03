class Ship:
    """
        Представление информации о кораблях..

        Args:
            name (str)    : Название корабля.
            tonnage (int) : Грузоподъемность корабля.
            speed (int)   : Скорость корабля.
            armament (int): Вооружение коробля.

        Returns:
            str: Информация о корабле.
        """
    def __init__(self,
                 name : str = 'Название',
                 tonnage : int = 'грузоподъёмность',
                 speed : int = 'скорость',
                 armament : str = 'вооружение'):
        self.name = name
        self.tonnage = tonnage
        self.speed = speed
        self.armament = armament

    def describe_ship(self):
        return (f"\n============================================\n"
                f"Корабль '{self.name}' : {self.tonnage} тонн\n\t"
                f"скорость : {self.speed}\n\t"
                f"вооружён : {self.armament}")

    def __str__(self):
        return self.describe_ship()

class Frigate(Ship):
    def __init__(self,
                 name,
                 tonnage,
                 speed,
                 armament,
                 anti_submarine_defense = True): # противолодочное оружие
        super().__init__(name, tonnage, speed, armament)
        self.anti_submarine_defense = anti_submarine_defense

    def has_antisubmarine_defense(self):
        return self.anti_submarine_defense

    def __str__(self):
        if self.anti_submarine_defense:
            defense_str = ("\nИмеет противолодочную оборону"
                           "\n============================================\n")
        else:
            defense_str = ("\nНе имеет противолодочной обороны"
                           "\n============================================\n")

        return f"Фрегат {super().__str__()} и {defense_str}."

class Destroyer(Ship):
    def __init__(self,
                 name,
                 tonnage,
                 speed,
                 armament,
                 radar_system):
        super().__init__(name, tonnage, speed, armament)
        self.radar_system = radar_system # система радаров

    def describe_radar_system(self):
        return (f"Современная система радаров: {self.radar_system}"
                f"\n============================================\n")

    def __str__(self):
        return (f"Эсминец {super().__str__()}\n"
                f"Оснащен {self.describe_radar_system()}.")

class Cruiser(Ship):
    def __init__(self,
                 name,
                 tonnage,
                 speed,
                 armament,
                 autonomy_days):
        super().__init__(name, tonnage, speed, armament)
        self.autonomy_days = autonomy_days

    def describe_autonomy(self):
        return f"Автономностью: {self.autonomy_days} суток."

    def __str__(self):
        return (f"Крейсер {super().__str__()}\n"
                f"Оснащен {self.describe_autonomy()}.\n"
                f"============================================")


def get_user_input():
    while True:
        ship_tipe = input("Выберите тип корабля: \n"
                          "1. Фрегат\n"
                          "2. Эсминец\n"
                          "3. Крейсер\n"
                          "Введите цифру: ").strip()

        if ship_tipe not in ('1', '2', '3'):
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

        # Общие данные для всех кораблей
        name = input("Введите название корабля: ")
        tonnage = int(input("Введите грузоподъёмность корабля (тонны): "))
        speed = int(input("Введите скорость корабля (узлы): "))
        armament = input("Введите вооружение корабля: ")

        # Выбор конкретного корабля и создание объекта
        if ship_tipe == '1':
            anti_submarine_defense = input("Имеет ли противолодочную оборону?\n"
                                           "1. Да\n"
                                           "2. Нет\n=======\n") == '1'
            print(f"============================================\n")
            return Frigate(name,
                           tonnage,
                           speed,
                           armament,
                           anti_submarine_defense)

        elif ship_tipe == '2':
            radar_system = input("Введите название системы радаров: ")
            print(f"============================================\n")
            return Destroyer(name,
                           tonnage,
                           speed,
                           armament,
                           radar_system)

        elif ship_tipe == '3':
            autonomy_days = int(input("Введите автономность корабля (сутки): "))
            print(f"============================================\n")
            return Cruiser(name,
                           tonnage,
                           speed,
                           armament,
                           autonomy_days)

if __name__ == "__main__":
    user_ship = get_user_input()
    print(user_ship)
