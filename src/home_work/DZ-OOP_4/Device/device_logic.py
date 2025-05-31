class Menu:
    def __init__(self):
        pass

    def control_device(self, device): # Что сделать с выключателем?
        """Меню управления выбранным выключателем"""
        while True:
            print(f"{'=' * 20}")
            print("1 Вкл/Выкл")
            print("+ Добавить скорость")
            print("- Убавить скорость")
            print("0 Состояние")
            print(f"{'-' * 20}")
            print("Enter : Выйти в Меню")
            print(f"{'=' * 20}")

            us_inp = input("\nВыбор действия: ")

            if us_inp == '':
                print("Выход в меню...")
                break
            elif us_inp == '1':
                device.devicePower()
            elif us_inp == '+':
                device.levelUp()
            elif us_inp == '-':
                device.levelDown()
            elif us_inp == '0':
                device.show()
            else:
                print("Некорректный ввод.\nПопробуйте снова.")