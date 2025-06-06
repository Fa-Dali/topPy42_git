from datetime import datetime

# Основная функция для отображения текущего времени
def show_current_time():
    current_time = datetime.now().strftime('%H:%M')
    print(current_time)

# Декоратор, который добавляет оформление (звёздочки сверху и снизу)
def decorate_with_stars(func):
    def wrapper():
        print('**************************')
        func()
        print('**************************')
    return wrapper

# Применение декоратора к функции show_current_time
decorated_show_time = decorate_with_stars(show_current_time)

# Вызываем декорированную функцию
decorated_show_time()