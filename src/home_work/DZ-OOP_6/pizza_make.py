# Базовый класс для пиццы
class Pizza:
    def cost(self):
        return 0

    def description(self):
        return ""

# Декораторы для добавок
class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def cost(self):
        return self.pizza.cost()

    def description(self):
        return self.pizza.description()

# Ингредиенты для пиццы (декораторы)
class TomatoSauceDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 5

    def description(self):
        return self.pizza.description() + ",\n\t томатный соус"

class MozzarellaCheeseDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 10

    def description(self):
        return self.pizza.description() + ",\n\t моцарелла"

class BasilicDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 3

    def description(self):
        return self.pizza.description() + ",\n\t базилик"

class CheddarDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 8

    def description(self):
        return self.pizza.description() + ",\n\t чеддер"

class BlueCheeseDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 12

    def description(self):
        return self.pizza.description() + ",\n\t сыр чизз"

class ProsciuttoDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 15

    def description(self):
        return self.pizza.description() + ",\n\t прошутто"

class HamDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 10

    def description(self):
        return self.pizza.description() + ",\n\t ветчина"

class PineappleDecorator(Decorator):
    def cost(self):
        return self.pizza.cost() + 7

    def description(self):
        return self.pizza.description() + ",\n\t ананас"

# Базовая основа
class PlainPizza(Pizza):
    def cost(self):
        return 50

    def description(self):
        return "Пицца"

# Пользователь выбирает ингридиенты
def interactive_pizza_builder():
    ingredients = {
        "1": TomatoSauceDecorator,
        "2": MozzarellaCheeseDecorator,
        "3": BasilicDecorator,
        "4": CheddarDecorator,
        "5": BlueCheeseDecorator,
        "6": ProsciuttoDecorator,
        "7": HamDecorator,
        "8": PineappleDecorator
    }

    pizza = PlainPizza()
    print(f"Основа пицы: {pizza.cost()} рублей")
    print("\nСоздайте свою пиццу.")

    while True:
        print("\n  Доступные ингредиенты:")
        print("=========================")
        print("1. Томатный соус :5  руб)")
        print("2. Моцарелла ... :10 руб)")
        print("3. Базилик ..... :3  руб)")
        print("4. Чеддер ...... :8  руб)")
        print("5. Сыр ......... :12 руб)")
        print("6. Прошутто .... :15 руб)")
        print("7. Ветчина ..... :10 руб)")
        print("8. Ананас ...... :7  руб)")
        print("=========================")
        print("Пробел : .......... Выход")
        print("Ввод . : ......... Готово")
        print("=========================")


        choice = input("Выберите номер ингридиента\n")

        if choice.strip() == '':
            break

        elif choice in ingredients.keys():
            pizza = ingredients[choice](pizza)
            print("\n==================================")
            print(f"Ингридиенты: {pizza.description()}")
            print(f"Текущая стоимость: {pizza.cost():,d} рублей.")
            print("==================================")

        else:
            print("Ошибка: такого ингредиента нет.\n"
                  "Попробуйте ещё.")

    return pizza

# Удаление последнего ингредиента
def remove_last_ingredient(pizza):
    # Удаляем последний слой, если это возможно.
    if isinstance(pizza, Decorator):
        return pizza.pizza
    else:
        return pizza

# Интерфейс ползователя
def user_interface():
    pizza = interactive_pizza_builder()

    while True:
        print("\nВыбирайте следующую операцию:")
        print("1. Завершить составление пиццы")
        print("2. Удалить последний ингредиент")
        operation_choice = input("Ваш выбор (1 или 2): ")

        if operation_choice == '1':
            print("\nВаша пицца готова!")
            print(f"Цена: {pizza.cost()} рублей")
            print(f"Состав: {pizza.description()}")
            break

        elif operation_choice == '2':
            pizza = remove_last_ingredient(pizza)
            print("\nПоследний ингредиент удалён.")
            print(f"Новая стоимость: {pizza.cost()} рублей")
            print(f"Новые ингредиенты: {pizza.description()}\n")

        else:
            print("Ошибка: некорректный выбор.\n"
                  "Попробуйте снова.")

if __name__ == "__main__":
    user_interface()