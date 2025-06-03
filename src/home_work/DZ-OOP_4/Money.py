import locale
locale.setlocale(locale.LC_NUMERIC, 'ru_RU.UTF-8')

class Money:
    '''Класс для работы с денежными суммами.'''

    def __init__(self,
                 money = 0,
                 penny = 0) -> None:
        '''
        Конструктор класса:
        :param money: цельная часть суммы
        :param penny: дробная часть суммы
        '''
        self.money = money
        self.penny = penny

    def display(self) -> None:
        '''
        Метод для вывода суммы на экран
        :return: 00.00
        '''
        print(f"{self.money}.{self.penny:02d}")

    def set_money(self, money) -> None:
        '''
        Метод для задания цельной части суммы.
        :param money:
        :return:
        '''
        self.money = money

    def set_penny(self, penny) -> None:
        '''
        Метод для задания дробной части суммы.
        :param penny:
        :return:
        '''
        self.penny = penny

def us_inp():
    '''
    Запрос пользователю размера суммы.
    :param money:
    :param penny:
    :return: рубли и копейки
    '''
    print("Введите сумму")
    print("===========================")
    currency = input("Введите валюту : ")
    money = int(input("- цельная часть суммы : "))
    penny = int(input("- дробная часть суммы : "))
    print()
    return money, penny, currency

def user_name():
    name = input("Введите ваше имя : ")
    return name

def show_money(name, money, penny, currency):
    '''
    Показывает информацию о сумме и валюте пользователя.
    :param name: имя пользователя
    :param money: цельная часть суммы
    :param penny: дробная часть суммы
    :param currency: валюта
    '''
    o_account = Money(money, penny)

    cap = f"= СЧЁТ ПОЛЬЗОВАТЕЛЯ : {name} ==========="
    money_table = f"{locale.format_string('%d', o_account.money, grouping=True)}.{o_account.penny:02d} рублей"

    print(cap)
    print(f"| Валюта: {currency:<29}|")
    print("-" * len(cap))
    print(f"| Сумма : "
          f"{money_table.center(29)}|")
    print("=" * len(cap))
    print()

if __name__ == "__main__":
    # name = user_name()
    name ='Сергей'
    money, penny, currency = us_inp()
    show_money(name, money, penny, currency)
