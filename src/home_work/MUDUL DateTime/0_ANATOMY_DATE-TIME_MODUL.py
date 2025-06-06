'''
Представь, что у тебя есть волшебные часы, которые умеют запоминать любое
время и любую дату. Это и есть библиотека `datetime` в Python.

📅 🕰️

В Python есть специальная коробка (библиотека), которая называется `datetime`.
Она помогает компьютеру запомнить и посчитать даты и время. Давай разберемся,
как она устроена:

### Что умеет эта магическая коробочка?

✨ **Она хранит дни и минуты:**
Может запомнить сегодняшний день, вчерашний день или
день рождения твоей бабушки.

⏳ **Помогает считать время:**
Узнать, сколько прошло часов или минут между сегодняшним утром и вечером.

🔥 **Делает календарь:**
Знает, сколько дней в месяце, какой день недели и многое другое.

### Посмотрим на простые команды:

1. **Сегодняшняя дата:**
'''
today = datetime.date.today()
print(today)
'''
    Это значит: спроси у компьютера, какой сегодня день.

2. **Точное время:**  
'''
now = datetime.datetime.now()
print(now)
'''
    Спрашивает компьютер точное время прямо сейчас.

3. **Посчитать разницу между датами:**  
    Например, узнать, сколько дней осталось до Нового Года:
'''
new_year = datetime.date(2025, 1, 1)
days_left = new_year - today
print(days_left.days)
'''

### Зачем это нужно?

- Узнать возраст кого-то: "Какой твой день рождения?" ➡️ Посмотреть, 
сколько лет исполнилось.
- Сделать таймер: "Через пять минут звони мне!"
- Следить за сроками уроков или мероприятий: "До начала каникул осталось..."

### Простой вывод:  
Библиотека `datetime` — это как умные часы и календарь в одном флаконе. 
Она умеет хранить и считать даты и время, помогая решать кучу интересных задач.

========================================================================
        ВСЕ МЕТОДЫ РАБОТЫ С datetime
========================================================================

Библиотека `datetime` в Python предоставляет мощные средства для работы 
с датами и временем. Ниже представлен обзор основных классов и методов, 
позволяющих манипулировать датами, временными интервалами и календарными 
операциями.

### Основные классы библиотеки `datetime`

1. **`datetime.date`**  
   Класс для представления даты (день, месяц, год).

2. **`datetime.time`**  
   Класс для хранения времени суток (час, минута, секунда, микросекунды).

3. **`datetime.datetime`**  
   Объединяет дату и время в одно целое.

4. **`datetime.timedelta`**  
   Объект для представления интервала времени (разница между двумя датами 
   или временами).

5. **`datetime.tzinfo`**  
   Абстрактный класс для временной зоны (используется редко).

### Ключевые методы и свойства

#### 1. **Создание объектов даты и времени**
- **`today()`**  
  Возвращает текущую локальную дату (без времени).
'''
date_today = datetime.date.today()
'''
- **`now()`**  
  Получает текущую дату и время (локально или с указанием временной зоны).
'''
current_time = datetime.datetime.now()
'''
- **`utcnow()`**  
Получить текущее время UTC (Universal Time Coordinated).
'''
utc_current_time = datetime.datetime.utcnow()
'''
- **`fromtimestamp(timestamp)`**  
Создает объект даты/времени из Unix timestamp (количество секунд с 1 января 1970 года).
'''
dt = datetime.datetime.fromtimestamp(1672531200)
'''
- **`combine(date, time)`**  
Объединяет отдельные объекты даты и времени в один объект `datetime`.
'''
combined_dt = datetime.datetime.combine(some_date, some_time)
'''
- **`strftime(format)`**  
Форматирует дату и время в строку по указанному формату.
'''
formatted_string = dt.strftime("%Y-%m-%d %H:%M:%S")
'''
- **`strptime(string, format)`**  
Парсит строку в объект даты/времени по заданному формату.
'''
parsed_dt = datetime.datetime.strptime('2023-12-31', "%Y-%m-%d")
'''

#### 2. **Операции с объектами даты и времени**
- **`replace(year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=True, fold=False)`**  
Замещает поля объекта даты/времени новыми значениями.
'''
new_dt = old_dt.replace(hour=12)
'''
- **`timetuple()`**  
Преобразует объект даты/времени в кортеж формата struct_time.
'''
tuple_representation = dt.timetuple()
'''
- **`timestamp()`**  
Преобразует объект даты/времени в Unix timestamp (секунды с эпохи).
'''
unix_timestamp = dt.timestamp()
'''
- **`weekday()`**  
Возвращает номер дня недели (0 — понедельник, ..., 6 — воскресенье).
'''
weekday_number = dt.weekday()
'''
- **`isoweekday()`**  
Аналогично `weekday()`, но нумерация начинается с 1 (понедельник).
'''
iso_weekday = dt.isoweekday()
'''
- **`ctime()`**  
Формирует удобочитаемую строку даты и времени.
'''
readable_string = dt.ctime()
'''

#### 3. **Разница между датами и временем (`timedelta`)**
- **`total_seconds()`**  
Возвращает полное количество секунд в timedelta.
'''
diff_in_seconds = delta.total_seconds()
'''
- **`days`**  
Количество дней в timedelta.
'''
number_of_days = delta.days
'''
- **`seconds`**  
Число секунд в timedelta (менее суток).
'''
seconds_part = delta.seconds
'''
- **`microseconds`**  
Микросекундная составляющая timedelta.
'''
microseconds_part = delta.microseconds
'''

### Типичные сценарии использования
1. **Определение возраста по дате рождения:**
'''
 birth_date = datetime.date(1990, 1, 1)
 age = datetime.date.today().year - birth_date.year
'''
2. **Форматирование даты в удобочитаемый вид:**
'''
event_date = datetime.datetime(2023, 12, 31, 23, 59)
formatted_event = event_date.strftime('%A, %B %d, %Y at %I:%M%p')
'''
3. **Расчет разницы между двумя датами:**
'''
first_day = datetime.date(2023, 1, 1)
last_day = datetime.date(2023, 12, 31)
difference = last_day - first_day
print(difference.days)
'''

Эти методы покрывают большинство повседневных задач, связанных с 
манипуляцией датами и временем в Python.


Да, конечно! Помимо тех методов, которые я описал ранее, библиотека 
`datetime` предоставляет ещё несколько полезных методов и свойств, 
которые пригодятся при работе с датами и временем. Расширю предыдущую 
информацию дополнительными возможностями.

### Дополнительные методы и свойства
#### 1. **Форматы вывода даты и времени**
- **`isoformat()`**  
  Возвращает строковое представление даты или времени в ISO-формате 
  (стандарт ISO 8601).
'''
dt = datetime.datetime.now()
iso_formatted = dt.isoformat()
'''
- **`astimezone(timezone)`**  
  Преобразует объект `datetime` в указанный часовой пояс (возвращает 
  копию с новым объектом временной зоны).
'''
local_time = datetime.datetime.now()
utc_time = local_time.astimezone(datetime.timezone.utc)
'''
- **`utcoffset()`**  
  Возвращает смещение относительно UTC (для объектов с временной зоной).
'''
offset = dt.utcoffset()
'''
- **`tzname()`**  
  Возвращает имя временной зоны (если установлено).
'''
timezone_name = dt.tzname()
'''
- **`dst()`**  
  Информация о переходе на летнее время (DST, Daylight Saving Time).
'''
daylight_saving = dt.dst()
'''

#### 2. **Разбор и формирование временных меток**

- **`toordinal()`**  
  Преобразует дату в число дней с момента условного нуля 
  (1 января 1 года).
'''
ordinal_value = dt.toordinal()
'''
- **`fromordinal(day_number)`**  
  Преобразует число дней обратно в дату.
'''
original_date = datetime.date.fromordinal(ordinal_value)
'''
- **`utctimetuple()`**  
  Возвращает структуру времени в виде кортежа для UTC.
'''
utc_tuple = dt.utcnow().utctimetuple()
'''
- **`fold`**  
  Параметр, используемый при создании объектов с неопределенной 
  информацией о DST (летнем времени); помогает выбрать правильное 
  время в случаях двусмысленности.
'''
ambiguous_dt = datetime.datetime(2023, 10, 29, 2, 30, fold=1)
'''

#### 3. **Манипуляции с временной зоной**

- **`timezone.utc`**  
  Стандартный объект временной зоны UTC.
'''
utc_zone = datetime.timezone.utc
'''
- **`pytz` (сторонняя библиотека)**  
  Часто используется для удобной работы с часовыми поясами и 
  переходами на летнее время.
'''
from pytz import timezone
moscow_tz = timezone('Europe/Moscow')
localized_dt = dt.astimezone(moscow_tz)
'''

### Примеры использования

1. **Определить ближайший рабочий день 
(исключая субботу и воскресенье):**
'''
def next_workday(dt):
   while dt.weekday() >= 5:  # Суббота и воскресенье
       dt += datetime.timedelta(days=1)
   return dt

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
next_business_day = next_workday(tomorrow)
'''
2. **Переключение временного пояса:**
'''
ny_time = datetime.datetime.now(datetime.timezone.utc).astimezone(pytz.timezone('America/New_York'))
'''
3. **Параметры сравнения дат:**
'''
birthday = datetime.date(1990, 1, 1)
if birthday > datetime.date.today():
   print("Ваш день рождения ещё впереди!")
'''

Эти методы и приемы помогут значительно облегчить вашу жизнь при 
управлении временем и датами в Python. Если нужны ещё примеры или 
углубленный разбор какого-то конкретного аспекта, обращайтесь!

========================================================================
            ДЛЯ МЕБЕЛЬНОГО БИЗНЕСА
========================================================================

Работа с датами и временем важна практически для любого бизнеса, и 
мебельное производство не исключение. Я подготовил десять конкретных 
примеров того, как библиотека `datetime` может принести пользу в 
повседневной деятельности мебельной фабрики.

### Примеры использования `datetime` в мебельном производстве

#### 1. **Планирование сроков поставок клиентам**
Нужно рассчитать, сколько времени осталось до окончания срока 
поставки заказа:
'''
delivery_deadline = datetime.date(2023, 12, 31)
current_date = datetime.date.today()
remaining_days = (delivery_deadline - current_date).days
if remaining_days <= 10:
    print("Осталось меньше 10 дней до завершения заказа!")
'''
#### 2. **Оценка скорости выполнения заказа**
Рассчитывать среднее время производства одного изделия:
'''
order_start = datetime.datetime(2023, 10, 1)
completed_at = datetime.datetime(2023, 10, 15)
production_duration = completed_at - order_start
average_time_per_piece = production_duration / quantity
'''
#### 3. **Управление запасами материалов**
Регистрация прихода и расхода запасов материалов:
'''
material_arrival = datetime.datetime.now()
expiration_date = material_arrival + datetime.timedelta(months=6)
print(f"Срок годности истекает {expiration_date}.")
'''
#### 4. **Логирование истории заказов**
Ведётся журнал записей с отметками времени приема и отправки заказов:
'''
log_entry = (f"Приняли заказ №1234 в "
             f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
'''
#### 5. **Расчёт времени гарантийного обслуживания**
Установить дату истечения гарантии на произведённую мебель:
'''
purchase_date = datetime.date(2023, 1, 1)
warranty_period = purchase_date + datetime.timedelta(years=2)
print(f"Ваша гарантия заканчивается {warranty_period}.")
'''
#### 6. **Анализ загрузки оборудования**
Изучение среднего времени занятости станков и оборудования:
'''
machine_started = datetime.datetime(2023, 10, 1, 8, 0)
machine_stopped = datetime.datetime(2023, 10, 1, 17, 0)
downtime = machine_stopped - machine_started
print(f"Машина работала {downtime}.")
'''
#### 7. **Календарь ремонтных работ**
Организация планового технического обслуживания оборудования:
'''
maintenance_schedule = [
    {"date": datetime.date(2023, 10, 15)},
    {"date": datetime.date(2023, 11, 1)}
]
for entry in maintenance_schedule:
    print(entry['date'].strftime("%d.%m.%Y"))
'''
#### 8. **Автоматическое уведомление сотрудников**
Отправка уведомлений сотрудникам о приближающемся дедлайне сдачи 
проекта:
'''
deadline = datetime.date(2023, 12, 31)
today = datetime.date.today()
if deadline - today <= datetime.timedelta(days=7):
    print("Внимание! Срок исполнения заказа близок.")
'''
#### 9. **Управляем расходниками и запчастями**
Система мониторинга наличия расходников и запчастей с ограниченным 
сроком службы:
'''
part_expiration = datetime.date(2023, 12, 31)
if part_expiration < datetime.date.today():
    print("Срок годности запчасти истек.")
'''
#### 10. **Контроль смен рабочих**
Организовать ротацию работников на смены с учётом времени работы:
'''
shift_start = datetime.datetime(2023, 10, 1, 8, 0)
shift_end = shift_start + datetime.timedelta(hours=8)
print(f"Смена началась в {shift_start} и закончится в {shift_end}.")
'''

Эти примеры показывают, насколько полезным может оказаться грамотное 
использование библиотеки `datetime` в процессе оптимизации работы 
мебельной фабрики, повышения точности расчетов и упорядоченности 
данных.

Я постарался показать широкий спектр ситуаций, где библиотека 
`datetime` может оказаться полезной для мебельного производства, 
но список далеко не исчерпывающий. Существуют десятки других кейсов, 
где знание работы с датами и временем существенно облегчает 
повседневные задачи.

Вот еще несколько распространенных и потенциально полезных вариантов 
применения:

### Еще 10 ситуаций использования `datetime` в мебельном бизнесе

#### 1. **Генерация отчетов по выполнению заказов**
Сортировка и фильтрация заказов по датам поступления и выполнения:
'''
orders = [
    {'id': 1, 'created_at': datetime.datetime(2023, 10, 1)},
    {'id': 2, 'created_at': datetime.datetime(2023, 10, 15)}
]
filtered_orders = [o for o in orders if o['created_at'] > datetime.datetime(2023, 10, 1)]
'''
#### 2. **Подсчет средней продолжительности ремонта**
Анализ времени ремонта дефектных изделий:
'''
repairs = [
    {'started_at': datetime.datetime(2023, 10, 1),
     'ended_at': datetime.datetime(2023, 10, 5)}
]
avg_repair_time = sum((r['ended_at'] - r['started_at']).total_seconds()
                      for r in repairs) / len(repairs)
'''
#### 3. **Маркетинговые акции по сезонам**
Проведение сезонных акций в определенные месяцы:
'''
today = datetime.date.today()
if today.month == 12:
    print("Акция зимнего ассортимента!")
'''
#### 4. **Прогноз продаж по историческим данным**
Анализ исторических данных о продаже мебели по периодам:
'''
sales_history = {
    datetime.date(2023, 1, 1): 100,
    datetime.date(2023, 2, 1): 120
}
this_month_sales = sales_history.get(datetime.date.today().replace(day=1))
'''
#### 5. **Сравнение времени выполнения заказов клиентов**
Вычислить средний срок выполнения заказов для разных регионов:
'''
orders_by_region = {
    'Москва': [
        {
            'start': datetime.datetime(2023, 10, 1),
            'finish': datetime.datetime(2023, 10, 10)
        }
    ],
    'Санкт-Петербург': [
        {
            'start': datetime.datetime(2023, 10, 1),
            'finish': datetime.datetime(2023, 10, 15)
        }
    ]
}
region_delivery_times = {}
for region, orders in orders_by_region.items():
    total_time = sum((o['finish'] - o['start']).days for o in orders)
    avg_time = total_time / len(orders)
    region_delivery_times[region] = avg_time
'''
#### 6. **График уборки и санитарии**
Регулярная уборка помещений и инвентаря с привязкой к расписанию:
'''
cleaning_schedule = datetime.datetime(2023, 10, 1, 10, 0)
next_cleaning = cleaning_schedule + datetime.timedelta(weeks=1)
'''
#### 7. **Планирование оплаты труда**
Просмотр зарплатного периода и расчет заработной платы:
'''
payroll_start = datetime.date(2023, 10, 1)
payroll_end = payroll_start + datetime.timedelta(days=30)
print(f"Зарплата начисляется за период с {payroll_start} "
      f"по {payroll_end}.")
'''
#### 8. **История модификаций товара**
Логирование изменений цены или характеристик изделия:
'''
product_modifications = []
product_modifications.append(
    {
        'change_date': datetime.datetime.now(),
        'new_price': 10000
    }
)
'''
#### 9. **Контроль посещаемости сотрудников**
Регистрация рабочего времени сотрудников и учет пропусков:
'''
employee_checkins = [
    {'employee_id': 1, 'checkin': datetime.datetime(2023, 10, 1, 9, 0)}
]
absent_employees = [emp for emp in employees
                    if all(emp['employee_id'] != checkin['employee_id']
                           for checkin in employee_checkins)]
'''
#### 10. **Заказы с учетом праздников**
Оптимизация расписания производства с учетом праздничных дней:
'''
holiday_dates = [datetime.date(2023, 12, 31)]  # Список праздничных дней
working_days = [(dt for dt in (datetime.date.today() + datetime.timedelta(n) for n in range(30)) if dt not in holiday_dates])
'''

### Итог
В заключение хочу подчеркнуть, что возможности библиотеки `datetime` 
в Python обширны и разнообразны. С их помощью можно решить огромное 
количество задач, будь то расчеты сроков выполнения заказов, ведение 
отчетности, мониторинг запасов или управление ресурсами на 
производстве. Изучив и освоив работу с датами и временем, вы 
откроете двери к повышению эффективности и надежности вашего бизнеса.

'''