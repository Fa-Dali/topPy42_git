from django.shortcuts import render
from datetime import datetime, timedelta

def current_datetime_view(request):
    # Получаем текущую дату и время
    current_datetime = datetime.now()

    # Формируем таблицу умножения
    table_data = [[i * j for j in range(1, 11)] for i in range(1, 11)]

    # Рассчитываем дату Дня программиста
    today = datetime.today()
    day_of_programmer = datetime(today.year, 1, 1) + timedelta(days=255)

    # Собираем весь контекст
    context = {
        'current_datetime': current_datetime,
        'table_data': table_data,
        'programmer_day': day_of_programmer,
    }

    return render(request, 'core/current_datetime.html', context)