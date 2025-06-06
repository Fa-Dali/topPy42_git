import datetime

# Основная функция для отображения текущего времени
def show_current_time():
    current_time = datetime.datetime.now().strftime('%d:%m:%Y')
    current_time1 = datetime.datetime.now().strftime('%H:%M')
    print(f"{current_time:^20}\n"
          f"{'-'*10:^20}\n"
          f"{current_time1:^20}")

# Первый декоратор: добавляем линии из звёздочек
def decorator_star_lines(func):
    def wrapper():
        print(' ' + '* ' * 10)
        func()
        print(' ' + '* ' * 10)
    return wrapper

# Второй декоратор: добавляем рамки из тире
def decorator_dash_border(func):
    def wrapper():
        print('-' * 21)
        func()
        print('-' * 21)
    return wrapper

# Сначала добавляем декоратор с линиями из звёздочек
show_current_time = decorator_star_lines(show_current_time)

# Потом добавляем декоратор с рамкой из тире
show_current_time = decorator_dash_border(show_current_time)

# Тестируем
show_current_time()