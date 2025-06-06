from abc import ABC, abstractmethod

# Интерфейс
class IPizza(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# Абстрактный класс
class Pizza(IPizza):
    def cost(self) -> float:
        return 0.0

    def description(self) -> str:
        return ""

# Декораторы для добавок
class Decorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def cost_it(self) -> float:
        return self.pizza.cost_its()

    def cost(self) -> float:
        return self.pizza.cost()

    def description(self) -> str:
        return self.pizza.description()

# Ингредиенты для пиццы (декораторы)
class TomatoSauceDecorator(Decorator):
    def cost_it(self):
        cost_its = 5.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + TomatoSauceDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + (f"\n{TomatoSauceDecorator.cost_it(self):>7} р.: томатный соус")

class MozzarellaCheeseDecorator(Decorator):
    def cost_it(self):
        cost_its = 10.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + MozzarellaCheeseDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + (f"\n{MozzarellaCheeseDecorator.cost_it(self):>7} р.: моцарелла")

class BasilicDecorator(Decorator):
    def cost_it(self):
        cost_its = 3.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + BasilicDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + (f"\n{BasilicDecorator.cost_it(self):>7} р.: базилик")

class CheddarDecorator(Decorator):
    def cost_it(self):
        cost_its = 8.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + CheddarDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + f"\n{CheddarDecorator.cost_it(self):>7} р.: чеддер"

class BlueCheeseDecorator(Decorator):
    def cost_it(self):
        cost_its = 12.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + BlueCheeseDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + (f"\n{BlueCheeseDecorator.cost_it(self):>7} р.: сыр чизз")

class ProsciuttoDecorator(Decorator):
    def cost_it(self):
        cost_its = 15.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + ProsciuttoDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + f"\n{ProsciuttoDecorator.cost_it(self):>7} р.: прошутто"

class HamDecorator(Decorator):
    def cost_it(self):
        cost_its = 10.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + HamDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + (f"\n{HamDecorator.cost_it(self):>7} р.: ветчина")

class PineappleDecorator(Decorator):
    def cost_it(self):
        cost_its = 7.00
        return cost_its

    def cost(self) -> float:
        return self.pizza.cost() + PineappleDecorator.cost_it(self)

    def description(self) -> str:
        return self.pizza.description() + f"\n{PineappleDecorator.cost_it(self):>7} р. : ананас"

# Базовая основа
class PlainPizza(Pizza):
    def cost_it(self):
        cost_its = 50.00
        return cost_its

    def cost(self) -> float:
        return 50.0

    def description(self) -> str:
        return f"\n{PlainPizza.cost(self):>7} р.: Пицца (основа)"

# Пользователь выбирает ингридиенты
def interactive_pizza_builder():
    ingredients = {                         # Создаем словарь составных пиццы
        "1": TomatoSauceDecorator,
        "2": MozzarellaCheeseDecorator,
        "3": BasilicDecorator,
        "4": CheddarDecorator,
        "5": BlueCheeseDecorator,
        "6": ProsciuttoDecorator,
        "7": HamDecorator,
        "8": PineappleDecorator
    }

    pizza = PlainPizza()                            # Создаем объект пицца

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
        print("0. : ............. Готово")
        print("=========================")


        choice = input("Выберите номер ингридиента\n")

        if choice.strip() == '0':
            break

        elif choice in ingredients.keys(): # если выбранный номер есть в
                                            # словаре
          # перем | номер ингредиента |в каком def искать
            pizza = ingredients[choice](pizza)
            print("\n==================================")
            print(f"Ингридиенты: {pizza.description()}")
            print("----------------------")
            print(f"ИТОГ: {pizza.cost():.2f} рублей.")
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
        print("Нельзя удалить больше ингредиентов:\n"
              "Вы можете отменить заказ пиццы.")
        return pizza

# Интерфейс ползователя
def user_interface():
    pizza = interactive_pizza_builder()



    while True:
        if pizza.cost() == 50.0:
            print("Вы отменили заказ.")
            break

        print("\nВыбирайте следующую операцию:")
        print("   0   : ........... Завершить")
        print("   -   : .. Удалить ингредиент")
        print("===============================")
        operation_choice = input("Ваш выбор: \n")


        if operation_choice == '0':
            if pizza.cost() == 50.0:
                print("Вы отменили заказ.")
                break
            else:
                print("\nВаша пицца готова!")
                print(f"Состав: {pizza.description()}")
                print(f"=============================")
                print(f"Цена: {pizza.cost():.2f} рублей")
                break

        elif operation_choice == '-':
            pizza = remove_last_ingredient(pizza)
            print("\nПоследний ингредиент удалён.")
            print(f"Новые ингредиенты: {pizza.description()}")
            print(f"=============================")
            print(f"Новая стоимость: {pizza.cost():.2f} рублей")


        else:
            print("Ошибка: некорректный выбор.\n"
                  "Попробуйте снова.")

if __name__ == "__main__":
    user_interface()