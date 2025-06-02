'''
Представь, что у тебя есть маленькая коробочка, куда ты складываешь свои
любимые игрушки. Иногда хочется положить туда что-то особенное, но надо
убедиться, что всё подходит по размеру и форме.

Метод `__setattr__(self, name, value)` в Python действует точно так же!
Представь, что это маленький охранник возле твоей коробки-игрушечницы.
Каждый раз, когда ты собираешься положить что-то внутрь (добавить атрибут
или поменять значение существующего), охранник внимательно осматривает предмет
и решает, можно ли его принять.

🎯 **Как это работает?**

Каждый раз, когда ты присваиваешь новому атрибуту значение или обновляешь
старый, Python сначала посылает сигнал этому самому охраннику (`__setattr__`),
который следит за процессом.

Приведу простой пример:
'''
class Кошель:
    def __setattr__(self, name, value):
        if name == "деньги":
            if value < 0:
                print("Нельзя хранить долги в кошельке!")
            else:
                super().__setattr__(name, value)
        else:
            super().__setattr__(name, value)

my_wallet = Кошель()
my_wallet.деньги = 100  # Всё нормально, деньги положили.
my_wallet.деньги = -50  # Охранник остановил попытку поставить минус.
'''
Итак, запомни:
- Всякий раз, когда ставишь или меняешь значение какого-то атрибута, 
        сначала оно проходит проверку методом `__setattr__`.
- Охранник может сказать «Да» или «Нет». Если «Да», атрибут принимает новое 
        значение. Если «Нет», атрибут остаётся прежним или выдается ошибка.

👍 **Для ребёнка главное понимать**, что `__setattr__` — это специальная 
проверка, которую проходят твои данные перед тем, как попасть в программу. 
Без неё было бы сложнее защититься от ошибок и ненужных сюрпризов!

=======================================
ХИТРОСТИ И НЮАНСЫ
=======================================

Метод `__setattr__(self, name, value)` — это особый инструмент, позволяющий 
перехватывать процесс установки любых атрибутов в вашем классе. Его правильное 
использование открывает массу возможностей, однако с ним связаны 
и определённые подводные камни. Разберём подробнее:

## 🎯 Основные хитрости и полезные приёмы

### 🔄 Интерцепция (перехват) установок атрибутов

Самое основное назначение `__setattr__` — возможность контроля за любыми 
попытками задать атрибут. Вы можете фильтровать устанавливаемые значения, 
проводить дополнительную логику или вовсе запрещать установку некоторых 
атрибутов.

Пример: ограничим диапазон допустимых значений атрибута `age`:
'''
class Person:
    def __setattr__(self, name, value):
        if name == 'age':
            if not (0 <= value <= 150):
                raise ValueError("Возраст должен быть от 0 до 150 лет.")
        object.__setattr__(self, name, value)

p = Person()
p.age = 30  # Установлено успешно
p.age = 200  # Будет вызвано исключение ValueError
'''
### 📌 Создание псевдо-переменных

Иногда удобно иметь набор фиктивных атрибутов, которыми пользователи могут 
манипулировать свободно, но которые фактически являются производными от других 
данных. В таком случае `__setattr__` помогает сохранить согласованность данных.

Пример: создадим объект с псевдополем `full_name`, 
состоящим из имени и фамилии:
'''
class Employee:
    def __setattr__(self, name, value):
        if name == 'full_name':
            first_name, last_name = value.split()
            self.first_name = first_name
            self.last_name = last_name
        else:
            object.__setattr__(self, name, value)

emp = Employee()
emp.full_name = "John Doe"  # Создаются два атрибута first_name и last_name
'''
### 🛠️ Настройка логики для вложенных объектов

Если ваши объекты содержат другие объекты (например, коллекции), вы можете 
использовать `__setattr__` для автоматической настройки внутренних элементов 
при изменении внешних атрибутов.

Пример: при установке нового размера корзины, автоматически увеличить 
вместимость внутреннего контейнера:
'''
class Basket:
    def __init__(self):
        self.items = []

    def __setattr__(self, name, value):
        if name == 'size':
            if value > len(self.items):
                self.items.extend([None]*(value - len(self.items)))
        object.__setattr__(self, name, value)

b = Basket()
b.size = 10  # Автоматом увеличивается размер списка items
'''
## 🦥 Нюансы и предостережения

### 🔇 Рекурсия и замыкающие циклы

Одна из частых ошибок новичков заключается в создании рекурсии при 
неправильном использовании `object.__setattr__(self, name, value)` 
внутри собственного метода `__setattr__`. Важно помнить, что внутренний 
вызов `object.__setattr__()` обязательно должен быть последним действием, 
иначе возникнет цикл.

Неправильно:
'''
class WrongExample:
    def __setattr__(self, name, value):
        self.name = value  # Это приведёт к бесконечной рекурсии
'''
Правильно:
'''
class CorrectExample:
    def __setattr__(self, name, value):
        if name == 'salary':
            if value < 0:
                raise ValueError("Зарплата не может быть меньше нуля.")
        object.__setattr__(self, name, value)  # Правильно заканчиваем цепочку
'''
### 🔒 Скрытость реализации

Использование `__setattr__` также создаёт интересный эффект: внешние клиенты 
вашей библиотеки не видят настоящей структуры хранения данных. Все манипуляции 
происходят через публичный интерфейс, а внутреннее устройство ваших классов 
скрыто.

Пример: хотя технически используется словарь `_attrs`, снаружи пользователь 
взаимодействует с объектами напрямую:
'''
class DataStore:
    def __init__(self):
        self._attrs = {}

    def __setattr__(self, name, value):
        if name != '_attrs':  # Чтобы избежать бесконечного цикла
            self._attrs[name] = value
        else:
            object.__setattr__(self, name, value)

ds = DataStore()
ds.value = 42  # Внешний мир думает, что это обычный атрибут
'''
## 📋 Итог

Правильное использование `__setattr__` открывает большие перспективы для 
оптимизации, защиты данных и добавления функциональности вашим объектам. 
Однако помните о подводных камнях, таких как возможные рекурсивные циклы и 
чрезмерная усложненность дизайна.

Применяйте его осторожно и продуманно, и ваша система станет намного мощнее 
и стабильнее.

Да, есть ещё пара интересных моментов, касающихся метода `__setattr__`, 
которые будут полезны для глубокого понимания темы:

## 📌 Дополнительные трюки и техники

### 🎬 Эмуляция динамических атрибутов

Можно использовать `__setattr__` совместно с `__getattr__`, чтобы имитировать 
существование атрибутов, которые не объявлены заранее.

Пример: создаем экземпляр, который хранит любую комбинацию атрибутов и 
возвращает их позже:
'''
class DynamicAttributes:
    def __setattr__(self, name, value):
        self.__dict__[name] = value  # Добавляем атрибут динамически

    def __getattr__(self, name):
        try:
            return self.__dict__[name]
        except KeyError:
            raise AttributeError(f"'DynamicAttributes' object "
                                 f"has no attribute '{name}'")

da = DynamicAttributes()
da.color = "blue"  # Атрибут color добавляется динамически
print(da.color)    # blue
'''
### 🪜 Регистрация изменений

Ещё одна полезная практика — ведение журнала изменений, регистрируя каждое 
присвоение атрибутов.

Пример: регистрируем историю изменений атрибута:
'''
class TrackedObject:
    def __init__(self):
        self.history = []

    def __setattr__(self, name, value):
        if name != 'history':
            self.history.append((name, value))
        object.__setattr__(self, name, value)

to = TrackedObject()
to.x = 10
to.y = 20
print(to.history)  # [(x, 10), (y, 20)]
'''
### 🚗 Сохранение старых значений

Можно сохранять предыдущее состояние атрибутов при каждом новом присвоении, 
обеспечивая поддержку истории изменений:
'''
class VersionedData:
    def __init__(self):
        self.previous_values = {}

    def __setattr__(self, name, value):
        if name in self.__dict__:
            old_value = self.__dict__.get(name)
            self.previous_values.setdefault(name, []).append(old_value)
        object.__setattr__(self, name, value)

vd = VersionedData()
vd.price = 100
vd.price = 150
print(vd.previous_values)  # {'price': [100]}
'''
## 📖 Советы по использованию

### 🩺 Пишите ясные условия

При написании условий в `__setattr__` старайтесь ясно выражать свою мысль, 
избегая запутанных конструкций. Лучше разбейте сложную логику на отдельные 
шаги, используя вспомогательные методы или функции.

### 🔍 Тестируйте на грани ограничений

Особенно важно тестировать крайние случаи, когда значение выходит за рамки 
ожидаемого диапазона. Напишите юнит-тесты, проверяющие границы возможных 
значений атрибутов.

### 📊 Используйте logging для диагностики

Иногда сложно отследить, какой атрибут вызвал проблемы. Включите логгирование 
в методе `__setattr__`, чтобы фиксировать имена атрибутов и значения, которые 
пытаются установить.

## 🔑 Подытожим

Мы рассмотрели различные аспекты использования метода `__setattr__`, включая 
динамическое создание атрибутов, регистрацию изменений и сохранение предыдущих 
состояний. Эти подходы помогут вам писать мощные и гибкие классы, способные 
адаптироваться к разным сценариям использования.

Главное правило — применять метод осознанно и аккуратно, учитывая все 
особенности и ограничения.

Чтобы запретить изменение конкретного атрибута в Python, можно воспользоваться 
специальным методом `__setattr__`. Основная задача этого метода — 
перехватывать попытки записи любого атрибута и реагировать на них 
соответствующим образом.

Давайте посмотрим пошагово, как это реализуется:

## 🎯 Алгоритм запрета изменения атрибута
1. Определяете, какие атрибуты должны быть неизменяемыми.
2. Перехватываете каждую попытку изменить атрибуты 
        с помощью метода `__setattr__`.
3. Внутри этого метода проверяете имя атрибута и запрещаете запись, если 
        атрибут является постоянным.

## 📌 Пример простого решения

Допустим, у вас есть класс `Car`, и вы хотите запретить изменение атрибута 
`vin_code` (VIN-код автомобиля), который задаётся единожды и далее 
не изменяется.
'''
class Car:
    def __init__(self, vin_code):
        self.vin_code = vin_code  # Первоначальное присвоение VIN-кода

    def __setattr__(self, name, value):
        if name == 'vin_code' and hasattr(self, 'vin_code'):
            raise AttributeError("Изменение VIN-кода невозможно.")
        object.__setattr__(self, name, value)

car = Car("ABC123DEF4567890")
try:
    car.vin_code = "XYZ987WXY1234567"  # Попытка изменить VIN-код
except AttributeError as e:
    print(e)  # Выведет: Изменение VIN-кода невозможно.
'''
### 📌 Что здесь произошло?
- Изначально атрибут `vin_code` установлен конструктором.
- Затем при попытке изменить его через оператор присваивания 
        срабатывает метод `__setattr__`.
- Поскольку условие `"if name == 'vin_code'"` выполняется, 
        генерируется исключение `AttributeError`, блокируя изменение атрибута.

## 👨‍🏫 Важные советы и рекомендации
- Обязательно убедитесь, что первоначальное присвоение атрибута возможно. 
        Например, конструктор класса может безопасно устанавливать постоянный 
        атрибут впервые.
- Помните, что наследники вашего класса тоже смогут пользоваться защитой 
        от перезаписи, если она правильно реализована.
- Учтите, что установка атрибутов через специальную конструкцию 
        `super().__setattr__(...)` пропускает вашу собственную защиту. 
        Поэтому убедитесь, что используемый вами родительский класс 
        (обычно `object`) не нарушает правил.

## 📚 Альтернативные способы защиты атрибутов

Помимо метода `__setattr__`, существуют и другие варианты блокировки атрибутов:

1. **Использовать дескриптор (descriptor)** — специализированные классы, 
        управляющие доступом к атрибутам.

2. **Сделать атрибут частным** (используя префикс подчеркивания `_`) и 
        документировать соглашение, что он неизменяемый.

Тем не менее, использование `__setattr__` остаётся одним из самых простых и 
        эффективных способов обеспечить гарантированную защиту атрибутов от 
        несанкционированных изменений.

=======================================
ДЛЯ БИЗНЕСА
=======================================

Метод `__setattr__` предлагает весьма ценные возможности для бизнеса, помогая 
решать практические задачи и улучшать архитектуру приложений. Рассмотрим 
конкретные сценарии, где его использование приносит пользу:

## 📌 Контроль доступа к важным данным

Многие бизнесы используют информационные системы, где защита данных играет 
ключевую роль. `__setattr__` позволяет строго регулировать доступ к атрибутам 
и гарантировать неприкосновенность важных сведений.

Пример: банковская система, где номер счёта должен оставаться неизменным после 
        первого задания:
'''
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number

    def __setattr__(self, name, value):
        if name == 'account_number' and hasattr(self, 'account_number'):
            raise AttributeError("Номер счёта не подлежит изменению.")
        object.__setattr__(self, name, value)
'''
Такое ограничение обеспечит уверенность, что данные остаются целостными и 
защищены от случайных модификаций.

## 💼 Оптимизация производительности и кэширование

Бизнес-приложения нередко обращаются к дорогостоящим внешним источникам 
данных (API, БД и т.д.). Применение `__setattr__` вместе с методами 
кеширования позволяет заметно ускорить работу приложений.

Пример: система, сохраняющая предыдущие состояния цены товара:
'''
class Product:
    def __init__(self):
        self.old_prices = []

    def __setattr__(self, name, value):
        if name == 'price':
            self.old_prices.append(getattr(self, 'price', None))
        object.__setattr__(self, name, value)
'''
Это сохраняет старые значения цен, что пригодится для анализа тенденций и 
аудита транзакций.

## 🧮 Стандартизация формата данных

Важнейшая задача большинства компаний — стандартизация данных. 
Правильная настройка процедуры назначения атрибутов позволяет 
привнести порядок в разнородные потоки информации.

Пример: платформа бронирования билетов контролирует формат номера рейса:
'''
class FlightBooking:
    def __setattr__(self, name, value):
        if name == 'flight_number':
            if re.match(r'[A-Z]{2}[0-9]{3}', str(value)):
                object.__setattr__(self, name, value.upper())
            else:
                raise ValueError("Некорректный формат номера рейса.")
        else:
            object.__setattr__(self, name, value)
'''
Это улучшает целостность данных и снижает риск ошибок, вызванных человеческими 
факторами.

## 🛠️ Логирование изменений и аудит

Практически любое серьёзное корпоративное ПО нуждается в протоколировании 
изменений ключевых показателей. Методом `__setattr__` можно организовать 
автоматическое журналирование.

Пример: журнал изменений статуса сотрудников:
'''
class Employee:
    def __init__(self):
        self.status_history = []

    def __setattr__(self, name, value):
        if name == 'status':
            current_status = getattr(self, 'status', None)
            self.status_history.append(current_status)
        object.__setattr__(self, name, value)
'''
Подобная функциональность полезна для отчётности и выявления нарушений 
регламента.

## 🔑 Гарантированная консистентность данных

Применение правильного подхода к назначению атрибутов обеспечивает 
стабильность и надежность системы. Компаниям важно держать свои данные в 
порядке и своевременно обнаруживать нарушения правил.

Пример: магазин, гарантирующий, что цены на товары указаны только целыми 
числами:
'''
class ShopItem:
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) != int:
                raise TypeError("Цена должна быть целым числом.")
        object.__setattr__(self, name, value)
'''

Это предотвратит появление дробных чисел, которые могут стать причиной 
путаницы и финансовых потерь.

## 📌 Вывод

Корректное использование метода `__setattr__` позволяет бизнесу достичь 
следующих целей:

- **Контролировать доступность данных** и препятствовать их 
        несанкционированному изменению.
- **Кэшировать дорогие операции**, повышая производительность системы.
- **Поддерживать стандарты представления данных**, улучшая их чистоту 
        и читаемость.
- **Логировать изменения**, обеспечивающей полную картину происходящего 
        в приложении.
- **Предупреждать конфликты и ошибки**, возникающие из-за неправильно 
        заданных значений.

Все эти факторы повышают устойчивость, эффективность и управляемость 
ИТ-инфраструктуры предприятия.

Хорошо, давайте рассмотрим десять практических примеров использования метода
 `__setattr__` с подробным описанием и рабочим кодом.

## 📌 Пример №1: Запрет изменения после первой установки
Представьте систему учёта активов, где уникальный идентификатор актива 
устанавливается однажды и не может меняться впоследствии.
'''
class Asset:
    def __setattr__(self, name, value):
        if name == 'id' and hasattr(self, 'id'):
            raise AttributeError("Идентификатор актива не может быть изменён.")
        object.__setattr__(self, name, value)

asset = Asset()
asset.id = 12345  # Первый раз устанавливается
try:
    asset.id = 67890  # Вторая попытка заканчивается исключением
except AttributeError as e:
    print(e)
'''
## 📌 Пример №2: Проверка типов данных
Система финансового учёта, где денежные суммы обязаны быть исключительно 
целочисленными значениями.
'''
class FinancialRecord:
    def __setattr__(self, name, value):
        if name == 'amount':
            if not isinstance(value, int):
                raise TypeError("Сумма должна быть целым числом.")
        object.__setattr__(self, name, value)

record = FinancialRecord()
record.amount = 1000  # Целое число — ОК
try:
    record.amount = 1000.50  # Десятичное число — ошибка
except TypeError as e:
    print(e)
'''
## 📌 Пример №3: Капитализация текста
Сайт новостей, где заголовки статей всегда приводятся к верхнему регистру
автоматически.
'''
class NewsArticle:
    def __setattr__(self, name, value):
        if name == 'title':
            value = value.upper()
        object.__setattr__(self, name, value)

article = NewsArticle()
article.title = "важная новость"  # Становится "ВАЖНАЯ НОВОСТЬ"
print(article.title)
'''
## 📌 Пример №4: Автоинкремент ID
Сервис бронирования отелей, где каждый заказ автоматически получает уникальный 
порядковый номер.
'''
class BookingOrder:
    _counter = 0

    def __setattr__(self, name, value):
        if name == 'order_id':
            BookingOrder._counter += 1
            value = BookingOrder._counter
        object.__setattr__(self, name, value)

order = BookingOrder()
order.order_id = ''  # Самозаданное автоинкрементируемое значение
print(order.order_id)
'''
## 📌 Пример №5: Приведение к нужному формату
Платформа электронной торговли, где почтовые индексы сохраняются только в
формате пятизначных цифр.
'''
class CustomerAddress:
    def __setattr__(self, name, value):
        if name == 'zip_code':
            if len(str(value)) != 5 or not str(value).isdigit():
                raise ValueError("Почтовый индекс должен содержать "
                                 "ровно пять цифр.")
        object.__setattr__(self, name, value)

address = CustomerAddress()
address.zip_code = 12345  # Подходит
try:
    address.zip_code = 'ABCD'  # Не пройдёт проверку
except ValueError as e:
    print(e)
'''
## 📌 Пример №6: Преобразование дат в ISO формат
CRM-система, где даты хранятся только в международном формате ISO (yyyy-mm-dd).
'''
from datetime import date

class ClientProfile:
    def __setattr__(self, name, value):
        if name == 'birth_date':
            if isinstance(value, date):
                value = value.isoformat()
            else:
                raise TypeError("Дата рождения должна быть объектом "
                                "datetime.date.")
        object.__setattr__(self, name, value)

client = ClientProfile()
client.birth_date = date.today()  # Дата преобразуется в ISO формат
print(client.birth_date)
'''
## 📌 Пример №7: Лимиты и фильтры
Магазин бытовой техники, где максимальная мощность устройства фиксируется 
заранее и не может превышать лимит.
'''
class Appliance:
    MAX_POWER = 2000  # Максимальная разрешенная мощность

    def __setattr__(self, name, value):
        if name == 'power':
            if value > Appliance.MAX_POWER:
                raise ValueError("Превышена допустимая мощность.")
        object.__setattr__(self, name, value)

appliance = Appliance()
appliance.power = 1500  # Нормально
try:
    appliance.power = 2500  # Провоцирует ошибку
except ValueError as e:
    print(e)
'''
## 📌 Пример №8: Хранение прошлых версий

ERP-система, где сохраняется история всех назначений атрибутов для 
последующего анализа.
'''
class HistoryTracker:
    def __init__(self):
        self.history = {}

    def __setattr__(self, name, value):
        if name != 'history':
            previous_value = getattr(self, name, None)
            self.history.setdefault(name, []).append(previous_value)
        object.__setattr__(self, name, value)

tracker = HistoryTracker()
tracker.temperature = 25
tracker.temperature = 30
print(tracker.history['temperature'])  # Показывает предыдущую температуру
'''
## 📌 Пример №9: Генерация уникальных токенов

Финансовый портал, где генерируются уникальные одноразовые коды для 
подтверждения платежей.
'''
import uuid

class TransactionToken:
    def __setattr__(self, name, value):
        if name == 'token':
            value = str(uuid.uuid4())[:8]  # Генерируем короткий UUID
        object.__setattr__(self, name, value)

transaction = TransactionToken()
transaction.token = ''
print(transaction.token)  # Уникальный токен будет сгенерирован автоматически
'''
## 📌 Пример №10: Полностью заблокированные атрибуты
Библиотека книг, где библиотечный инвентарный номер навсегда закреплён за 
каждым экземпляром.
'''
class LibraryBook:
    def __setattr__(self, name, value):
        if name == 'inventory_number':
            raise AttributeError("Инвентарный номер книги неизменяем.")
        object.__setattr__(self, name, value)

book = LibraryBook()
try:
    book.inventory_number = 12345  # Попытка невозможна
except AttributeError as e:
    print(e)
'''
## 📌 Заключение

Метод `__setattr__` даёт широкие возможности для эффективного управления 
атрибутами объектов, начиная от простых проверок и заканчивая сложными 
преобразованиями и контролем данных. Он позволяет обезопасить данные, 
упростить бизнес-процессы и повысить устойчивость системы к ошибкам.

Мебельное производство — отрасль, где важны точность измерений, соблюдение 
стандартов материалов и своевременность поставок. Я покажу, как метод
 `__setattr__` может помочь вашему производству на практике.
 
===========================
ДЛЯ МЕБЕЛЬНОГО ПРОИЗВОДСТВА
===========================

## 📌 Пример №1: Ограничение размеров изделий
Вероятно, вы работаете с большими массивами заготовок древесины, фанеры или 
МДФ. Очень важно отслеживать размеры изготавливаемых деталей, чтобы избежать 
перерасхода материала и брака.
'''
class FurniturePart:
    MAX_WIDTH = 120  # Максимально допустимая ширина изделия в см
    MAX_HEIGHT = 200  # Максимально допустимая высота изделия в см

    def __setattr__(self, name, value):
        if name == 'width' and value > FurniturePart.MAX_WIDTH:
            raise ValueError("Ширина превышает допустимый предел.")
        if name == 'height' and value > FurniturePart.MAX_HEIGHT:
            raise ValueError("Высота превышает допустимый предел.")
        object.__setattr__(self, name, value)

part = FurniturePart()
part.width = 100  # Нормально
try:
    part.height = 250  # Высота слишком большая
except ValueError as e:
    print(e)
'''
## 📌 Пример №2: Типы используемых материалов
Каждой мебели соответствует конкретный материал (дерево, пластик, металл 
и т.д.). Ваш завод производит продукцию из конкретных видов сырья, и смена 
материала возможна только после согласования.
'''
class Material:
    ALLOWED_TYPES = ['дуб', 'бук', 'осина']

    def __setattr__(self, name, value):
        if name == 'type':
            if value.lower() not in Material.ALLOWED_TYPES:
                raise ValueError("Материал не поддерживается.")
        object.__setattr__(self, name, value)

material = Material()
material.type = 'дуб'  # Допустимо
try:
    material.type = 'красное дерево'  # Материал не разрешён
except ValueError as e:
    print(e)
'''
## 📌 Пример №3: Ограничение минимального веса изделия
Вам важно, чтобы продукция была достаточно прочной и соответствовала
стандартам прочности. Один из индикаторов — вес готового изделия.
'''
class FinishedProduct:
    MIN_WEIGHT = 5  # Минимальный вес готовой мебели в кг

    def __setattr__(self, name, value):
        if name == 'weight' and value < FinishedProduct.MIN_WEIGHT:
            raise ValueError("Вес изделия ниже минимальной нормы.")
        object.__setattr__(self, name, value)

product = FinishedProduct()
product.weight = 7  # Вес нормальный
try:
    product.weight = 3  # Недостаточный вес
except ValueError as e:
    print(e)
'''
## 📌 Пример №4: Блокировка повторного обновления заказов
Ваше предприятие осуществляет поставки клиентам, и заказы обрабатываются 
поэтапно. После отправки заказа повторно изменить его характеристики 
недопустимо.
'''
class Order:
    STATUS_SENT = 'sent'

    def __setattr__(self, name, value):
        if (name == 'status' and hasattr(self, 'status')
                and self.status == Order.STATUS_SENT):
            raise AttributeError("Заказ уже отправлен и "
                                 "не подлежит изменениям.")
        object.__setattr__(self, name, value)

order = Order()
order.status = 'processing'  # Норма
order.status = Order.STATUS_SENT  # Отправлен
try:
    order.status = 'cancelled'  # Нельзя отменить отправленный заказ
except AttributeError as e:
    print(e)
'''
## 📌 Пример №5: Установка точной длины ножек стола
Очень важно, чтобы длина ножек столов и другой мебели была абсолютно 
одинаковой, иначе готовое изделие получится неровным. Таким образом, 
можно зафиксировать длину ножки и запретить её последующее изменение.
'''
class TableLeg:
    def __setattr__(self, name, value):
        if name == 'length' and hasattr(self, 'length'):
            raise AttributeError("Длина ножки зафиксирована и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

leg = TableLeg()
leg.length = 70  # Длина установлена
try:
    leg.length = 75  # Вторичное изменение приведет к исключению
except AttributeError as e:
    print(e)
'''
## 📌 Пример №6: Инвентаризация комплектующих
Каждая деталь мебели должна сопровождаться уникальным номером партии. 
Повторное изменение номера партии недопустимо.
'''
class InventoryItem:
    def __setattr__(self, name, value):
        if name == 'batch_number' and hasattr(self, 'batch_number'):
            raise AttributeError("Номер партии зафиксирован и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

item = InventoryItem()
item.batch_number = 'BATCH-001'  # Присвоение номера партии
try:
    item.batch_number = 'BATCH-002'  # Повторное изменение недопустимо
except AttributeError as e:
    print(e)
'''
## 📌 Пример №7: Форматы этикеток
Этикетка должна соответствовать строгим правилам маркировки. Она включает 
уникальный штрихкод, артикул и другую важную информацию. Надо удостовериться, 
что информация на этикетке правильная.
'''
class Label:
    REQUIRED_FIELDS = ['barcode', 'artikel']

    def __setattr__(self, name, value):
        if name in Label.REQUIRED_FIELDS and not value.strip():  # Проверка
                                            # заполнения обязательных полей
            raise ValueError("Этикетка не заполнена должным образом.")
        object.__setattr__(self, name, value)

label = Label()
label.barcode = '123456789'  # Нормально
try:
    label.artikel = ''  # Артикул пуст — ошибка
except ValueError as e:
    print(e)
'''
## 📌 Пример №8: Диапазон допустимой влажности древесины
Качество древесных материалов напрямую влияет на долговечность конечных 
изделий. Необходимо следить за уровнем влажности дерева, чтобы исключить 
порчу и деформацию готовых изделий.
'''
class WoodMaterial:
    HUMIDITY_RANGE = (8, 12)  # Проценты влажности

    def __setattr__(self, name, value):
        if (name == 'humidity'
                and not (WoodMaterial.HUMIDITY_RANGE[0] <= value
                         <= WoodMaterial.HUMIDITY_RANGE[1])):
            raise ValueError("Уровень влажности вне допустимого диапазона.")
        object.__setattr__(self, name, value)

wood = WoodMaterial()
wood.humidity = 10  # Уровень влажности правильный
try:
    wood.humidity = 15  # Высокий уровень влажности недопустим
except ValueError as e:
    print(e)
'''
## 📌 Пример №9: Гарантия сроков изготовления
Производитель обязуется поставлять готовые изделия вовремя. Любые задержки 
влияют на репутацию фирмы. Запрещаем изменять сроки сдачи проекта после 
утверждения графика.
'''
class ProjectSchedule:
    APPROVED_STATUS = 'approved'

    def __setattr__(self, name, value):
        if (name == 'delivery_date' and hasattr(self, 'status')
                and self.status == ProjectSchedule.APPROVED_STATUS):
            raise AttributeError("Срок поставки утверждён и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

schedule = ProjectSchedule()
schedule.delivery_date = '2025-12-31'  # Срок установлен
schedule.status = ProjectSchedule.APPROVED_STATUS  # Утверждён график
try:
    schedule.delivery_date = '2026-01-01'  # Новый срок недопустим
except AttributeError as e:
    print(e)
'''
## 📌 Пример №10: Серийный номер продукции
Каждое произведённое изделие должно иметь уникальный серийный номер, который 
сохраняется навсегда и не подлежит изменениям.
'''
class SerialNumber:
    def __setattr__(self, name, value):
        if name == 'serial' and hasattr(self, 'serial'):
            raise AttributeError("Серийный номер установлен и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

number = SerialNumber()
number.serial = 'FURNI-001'  # Установлен серийный номер
try:
    number.serial = 'FURNI-002'  # Новое значение недопустимо
except AttributeError as e:
    print(e)
'''
## 📌 Заключение
Метод `__setattr__` помогает настроить точные и надежные схемы управления 
данными в производстве мебели. Он позволяет наложить ограничения на 
измерительные параметры, материалы, габариты, статус исполнения заказов и 
многое другое. Ваша фабрика будет работать эффективнее, снизив брак и 
увеличив доверие заказчиков.

Для эффективного управления складом на мебельном производстве важно 
контролировать запасы материалов, готовых изделий и расходуемых компонентов. 
Метод `__setattr__` отлично подойдёт для реализации контроля и поддержания 
порядка на складе.

Вот восемь полезных сценариев использования `__setattr__` конкретно для 
склада на мебельном предприятии:

## 📌 Пример №1: Количество остатков материала
Необходимо чётко отслеживать остатки материалов на складе, чтобы не допустить 
нехватки или излишков. Любой заниженный остаток должен вызывать тревогу.
'''
class WarehouseStock:
    MIN_STOCK_LEVEL = 10  # минимальный запас

    def __setattr__(self, name, value):
        if name == 'quantity' and value < WarehouseStock.MIN_STOCK_LEVEL:
            raise ValueError("Запас недостаточен, пополните склад.")
        object.__setattr__(self, name, value)

stock = WarehouseStock()
stock.quantity = 15  # Осталось 15 единиц — норма
try:
    stock.quantity = 5  # Ниже минимума — выдаст ошибку
except ValueError as e:
    print(e)
'''
## 📌 Пример №2: Кодировка партий материалов
На складе используются специальные коды партий материалов, например, для 
древесины или фурнитуры. Эти коды уникальны и не подлежат изменениям после 
регистрации.
'''
class BatchCode:
    def __setattr__(self, name, value):
        if name == 'code' and hasattr(self, 'code'):
            raise AttributeError("Код партии установлен и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

batch = BatchCode()
batch.code = 'WOOD-BAT-001'  # Код установлен
try:
    batch.code = 'NEW-WOOD-CODE'  # Повторное изменение недопустимо
except AttributeError as e:
    print(e)
'''
## 📌 Пример №3: Проверка правильности упаковки
Перед отгрузкой вся продукция должна пройти обязательную упаковку. Необходимо 
отслеживать состояние упаковки ("упаковано"/"не упаковано").
'''
class PackagingStatus:
    VALID_STATES = ["upakovano", "ne_upakovano"]

    def __setattr__(self, name, value):
        if (name == 'packing_state' and value
                not in PackagingStatus.VALID_STATES):
            raise ValueError("Невалидный статус упаковки.")
        object.__setattr__(self, name, value)

package = PackagingStatus()
package.packing_state = "upakovano"  # Верный статус
try:
    package.packing_state = "sborochno"  # Незаконный статус
except ValueError as e:
    print(e)
'''
## 📌 Пример №4: Ограничение максимальной нагрузки паллет
Грузоподъёмность паллеты ограничена. Если превысить норму, груз будет 
перегруженным и опасным для транспортировки.
'''
class PalletLoad:
    MAX_LOAD = 500  # кг

    def __setattr__(self, name, value):
        if name == 'load_weight' and value > PalletLoad.MAX_LOAD:
            raise ValueError("Нагрузка превышает допустимую норму.")
        object.__setattr__(self, name, value)

pallet = PalletLoad()
pallet.load_weight = 450  # Загрузка нормальна
try:
    pallet.load_weight = 600  # Груз превышает норматив
except ValueError as e:
    print(e)
'''
## 📌 Пример №5: Сроки годности комплектующих
Комплектующие и фурнитуру необходимо регулярно проверять на свежесть. 
Каждая партия снабжается сроком годности, и важно убедиться, что этот 
срок действителен.
'''
from datetime import datetime

class ExpirationDate:
    def __setattr__(self, name, value):
        if name == 'expiration_date':
            today = datetime.now().date()
            expiration = datetime.strptime(value, "%Y-%m-%d").date()
            if expiration < today:
                raise ValueError("Срок годности истёк.")
        object.__setattr__(self, name, value)

furniture_part = ExpirationDate()
furniture_part.expiration_date = '2025-12-31'  # Годен
try:
    furniture_part.expiration_date = '2023-01-01'  # Истёкший срок годности
except ValueError as e:
    print(e)
'''
## 📌 Пример №6: Поддержание постоянного места хранения
Каждое помещение на складе должно быть использовано рационально, и 
местоположение груза после размещения не подлежит произвольному изменению.
'''
class StorageLocation:
    def __setattr__(self, name, value):
        if name == 'location' and hasattr(self, 'location'):
            raise AttributeError("Местоположение установлено и "
                                 "не подлежит изменению.")
        object.__setattr__(self, name, value)

storage = StorageLocation()
storage.location = 'Rack A1'  # Местоположение назначено
try:
    storage.location = 'Rack B2'  # Перемещение запрещено
except AttributeError as e:
    print(e)
'''
## 📌 Пример №7: Проверка ширины стеллажей
Стеллажи на складе имеют ограниченную ширину, и превышение габаритов может 
привести к повреждению оборудования и персонала.
'''
class ShelfWidth:
    MAX_WIDTH = 120  # Ширина полки в сантиметрах

    def __setattr__(self, name, value):
        if name == 'shelf_width' and value > ShelfWidth.MAX_WIDTH:
            raise ValueError("Ширина стеллажа превышает допустимое значение.")
        object.__setattr__(self, name, value)

shelf = ShelfWidth()
shelf.shelf_width = 100  # Норма
try:
    shelf.shelf_width = 150  # Превышен максимум
except ValueError as e:
    print(e)
'''
## 📌 Пример №8: Отслеживание уровней готовности изделий
Готовность изделий на складе важна для оперативного формирования отгрузки. 
Изделия должны находиться либо в статусе "готово", либо "на сборке".
'''
class ProductionStage:
    STAGES = ["ready", "assembly"]

    def __setattr__(self, name, value):
        if name == 'stage' and value not in ProductionStage.STAGES:
            raise ValueError("Недопустимый этап производства.")
        object.__setattr__(self, name, value)

production = ProductionStage()
production.stage = "ready"  # Готово
try:
    production.stage = "testing"  # Неправильный этап
except ValueError as e:
    print(e)
'''
## 📌 Заключение
Метод `__setattr__` помогает грамотно наладить управление ресурсами на 
складе, обеспечивая:

- Четкий контроль запасов и остатков материалов.
- Постоянство идентификационных данных (партии, серийные номера).
- Предотвращение ошибок при упаковке и маркировке продукции.
- Соблюдение нормативных ограничений по нагрузкам и размерам.
- Следование установленным срокам годности и регламентам эксплуатации.

Регулярное использование этого инструмента повысит эффективность работы склада 
и уменьшит потери из-за человеческой ошибки.
'''