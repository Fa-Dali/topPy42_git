'''
Модуль `json` в Python предоставляет несколько методов для работы с
JSON-данными. Вот основные из них:

### 1. **Сериализация (преобразование Python-объектов в JSON)**

- **`json.dumps(obj, *, skipkeys=False, ensure_ascii=True,
check_circular=True, allow_nan=True, cls=None, indent=None,
separators=None, default=None, sort_keys=False, **kw)`**
  Преобразует Python-объект в JSON-строку.
  - `obj`: Объект для сериализации.
  - `indent`: Определяет отступы для форматирования.
  - `sort_keys`: Сортирует ключи словаря.
  - `default`: Функция для обработки нестандартных типов.

- **`json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True,
check_circular=True, allow_nan=True, cls=None, indent=None,
separators=None, default=None, sort_keys=False, **kw)`**
  Записывает Python-объект в файл в формате JSON.
  - `fp`: Файловый объект для записи.

### 2. **Десериализация (преобразование JSON в Python-объекты)**

- **`json.loads(s, *, cls=None, object_hook=None, parse_float=None,
parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`**
  Преобразует JSON-строку в Python-объект.
  - `s`: JSON-строка.
  - `object_hook`: Функция для обработки объектов.
  - `parse_float`, `parse_int`, `parse_constant`: Функции для обработки
                                                    чисел и констант.

- **`json.load(fp, *, cls=None, object_hook=None, parse_float=None,
parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`**
  Читает JSON из файла и преобразует его в Python-объект.
  - `fp`: Файловый объект для чтения.

### 3. **Дополнительные методы**

- **`json.JSONEncoder`** и **`json.JSONDecoder`**
  Классы для кастомной сериализации и десериализации.
  - `JSONEncoder`: Позволяет переопределить метод `default`
                    для обработки нестандартных типов.
  - `JSONDecoder`: Позволяет переопределить метод `object_hook`
                    для обработки объектов.

### 4. **Примеры использования**

#### Сериализация:
'''
import json

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data, indent=4)
print(json_str)
'''

#### Десериализация:
'''
json_data = '{"name": "Bob", "age": 25}'
python_obj = json.loads(json_data)
print(python_obj)
'''

### 5. **Обработка ошибок**

- **`JSONDecodeError`**: Исключение, возникающее при ошибке десериализации.  

Эти методы позволяют эффективно работать с JSON-данными в Python, 
обеспечивая гибкость и удобство при обмене данными между приложениями.
========================================================================
'''
json.dumps(obj, *,
           skipkeys=False,
           ensure_ascii=True,
           check_circular=True,
           allow_nan=True,
           cls=None,
           indent=None,
           separators=None,
           default=None,
           sort_keys=False,
           **kw)
'''
========================================================================
В скобках указаны параметры функции json.dumps, которые определяют 
поведение процесса сериализации Python-объекта в JSON-строку. Вот их 
краткое описание:

obj: Объект, который нужно преобразовать в JSON-строку. 
        Это обязательный параметр.
skipkeys=False: Если True, пропускает ключи, которые не являются 
                строками, числами, булевыми значениями или None. 
                По умолчанию False.
ensure_ascii=True: Если True, все не-ASCII символы будут экранированы. 
                    По умолчанию True.
check_circular=True: Если True, проверяет наличие циклических ссылок 
                    в объекте. По умолчанию True.
allow_nan=True: Если True, допускает использование NaN, Infinity и -Infinity в JSON. По умолчанию True.
cls=None: Класс, который будет использоваться для сериализации. По умолчанию используется стандартный JSONEncoder.
indent=None: Определяет отступы для форматирования. Если None, используется компактный формат. По умолчанию None.
separators=None: Определяет разделители для ключей и значений. По умолчанию (', ', ': ').
default=None: Функция, которая будет вызываться для объектов, которые не могут быть сериализованы стандартным способом.
sort_keys=False: Если True, сортирует ключи словаря. По умолчанию False.
**kw: Дополнительные ключевые аргументы, которые могут быть переданы в функцию.
Эти параметры позволяют гибко настраивать процесс сериализации, обеспечивая соответствие требованиям конкретной задачи.
'''