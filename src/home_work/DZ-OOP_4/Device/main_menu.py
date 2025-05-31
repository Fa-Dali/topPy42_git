from Device import (CoffeeMachine, Blender, MeatGrinder)
from device_logic import Menu

def main():
    list_dimmers()

def list_dimmers():
    ''' объект: o_CoffeeMachine
        объект: o_Blender
        объект: o_MeatGrinder
    '''
    # определение объектов
    o_CoffeeMachine = CoffeeMachine()
    o_Blender = Blender()
    o_MeatGrinder = MeatGrinder()
    o_menu = Menu()

    while True:
        print(
            f" ======= АДМИН ПАНЕЛЬ ========================================+")
        print(f"        |    Кофемашина   |     Блендер     |    Мясорубка    |")
        print(
            f"--------|-----------------|-----------------|-----------------|")
        print(f"ПИТАНИЕ |"
              f"{'* ON *' if o_CoffeeMachine.switchIsOn else 'OFF':^17}|"
              f"{'* ON *' if o_Blender.switchIsOn else 'OFF':^17}|"
              f"{'* ON *' if o_MeatGrinder.switchIsOn else 'OFF':^17}|")
        print(
            f"--------|-----------------|-----------------|-----------------|")
        print(f"СКОРОСТЬ|"
              f"{o_CoffeeMachine.speed if o_CoffeeMachine.switchIsOn else '':^17}|"
              f"{o_Blender.speed if o_Blender.switchIsOn else '':^17}|"
              f"{o_MeatGrinder.speed if o_MeatGrinder.switchIsOn else '':^17}|")
        print(f"+=============================================================+")
        us_inp = input(
            "Выбрать |        1        |        2        |        3        "
            f"|\nВыберите номер устройства:\nEnter : Выход\n{'=' * 26}\n")

        # Активация нужного выключателя
        if us_inp == '':
            print("==========================")
            print("ПРИЛОЖЕНИЕ ОСТАНОВЛЕНО")
            break
        elif us_inp == '1':
            o_menu.control_device(o_CoffeeMachine)
        elif us_inp == '2':
            o_menu.control_device(o_Blender)
        elif us_inp == '3':
            o_menu.control_device(o_MeatGrinder)
        else:
            print("Неверный выбор. Повторите попытку.")


if __name__ == "__main__":
    main()