import threading
import random

# 🏫 Волшебный дневничок (локальное хранилище для пчёлок)
bee_diary = threading.local()

# 🐝 Отдельная функция для каждой пчёлки
def collect_nectar(beename, field):
    # 📚 Каждая пчёлка заводит запись в личном дневнике
    bee_diary.beename = beename
    bee_diary.field = field
    bee_diary.nectar_collected = 0

    # 🌿 Пчёлка собирается на цветок и собирает нектар
    print(f"🐝 Пчёлка {beename} отправилась на поле {field}.")
    collected_amount = random.randint(10, 50)  # Случайное количество собранного нектара
    bee_diary.nectar_collected += collected_amount
    print(f"🍯 Пчёлка {beename} собрала {collected_amount} капель нектара на поле {field}.")

# 🐝 Заводим несколько пчёлок
threads = []
fields = ['Ромашки', 'Васильки', 'Маковые луга']
names = ['Люси', 'Томми', 'Джеки']

for name, field in zip(names, fields):
    thread = threading.Thread(target=collect_nectar, args=(name, field))
    threads.append(thread)
    thread.start()

# 🏡 Ждём, пока пчёлки соберут нектар
for thread in threads:
    thread.join()

# 🍯 Смотрим, сколько собрали наши пчёлки
for name in names:
    print(f"📝 Пчёлка {name} собрала {bee_diary.nectar_collected} капель нектара.")