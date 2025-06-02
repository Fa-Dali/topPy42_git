# 0_0_Оформление_Docstring.py

'''
Оформление docstrings (докстрингов) играет ключевую роль в обеспечении хорошей
документации и поддержки кода. Правильно составленные докстринги улучшают
читаемость, помогают новым разработчикам быстрее освоить код и служат основой
для автоматизированной генерации документации.

В Python общепринятыми являются следующие стили оформления docstrings:

- Google Style Docstrings
- NumPy Style Docstrings
- reStructuredText (reST) Style

Рассмотрим каждый из них подробнее.

=================================
### 1. Google Style Docstrings
=================================
Google style предполагает следующую структуру:
'''
def my_function(arg1, arg2):
    """
    Brief description of the function.

    Extended description of the function can go here.

    Args:
        arg1 (type): Description of argument 1.
        arg2 (type): Description of argument 2.

    Returns:
        type: Description of what the function returns.

    Raises:
        ExceptionType: When something goes wrong.
    """
    pass
'''
Основные компоненты:
- **Краткое описание:** Однострочное резюме функции.
- **Подробное описание:** Более развернутое объяснение работы функции.
- **Args:** Список аргументов с указанием их типов и назначения.
- **Returns:** Тип возвращаемого значения и описание результата.
- **Raises:** Возможные исключения, генерируемые функцией.

Пример использования:
'''
def multiply_numbers(a, b):
    """
    Умножает два числа.

    Эта функция умножает два целых числа и возвращает результат.

    Args:
        a (int): Первое целое число.
        b (int): Второе целое число.

    Returns:
        int: Произведение двух чисел.
    """
    return a * b
'''

=================================
### 2. NumPy Style Docstrings
=================================
NumPy style основан на схожей концепции, 
но с небольшими отличиями в оформлении:
'''
def my_function(arg1, arg2):
    """
    Brief description of the function.

    Extended description of the function can go here.

    Parameters
    ----------
    arg1 : type
        Description of argument 1.
    arg2 : type
        Description of argument 2.

    Returns
    -------
    type
        Description of what the function returns.

    Raises
    ------
    ExceptionType
        When something goes wrong.
    """
    pass
'''

Основные компоненты:
- **Parameters:** Раздел для описания аргументов функции.
- **Returns:** Информация о результате работы функции.
- **Raises:** Возможные исключения.

Пример использования:
'''
def calculate_mean(numbers):
    """
    Рассчитывает среднее арифметическое элементов массива.

    Parameters
    ----------
    numbers : list or array-like
        Входной массив чисел.

    Returns
    -------
    float
        Среднее арифметическое чисел.

    Raises
    ------
    ZeroDivisionError
        Если массив пуст.
    """
    if len(numbers) == 0:
        raise ZeroDivisionError("Список чисел пуст")
    return sum(numbers) / len(numbers)
'''
=====================================
### 3. reStructuredText (reST) Style
=====================================

Формат reStructuredText популярен для подготовки документации с использованием 
инструментов вроде Sphinx:
'''
def my_function(arg1, arg2):
    """
    Brief description of the function.

    :param arg1: Description of argument 1.
    :type arg1: type
    :param arg2: Description of argument 2.
    :type arg2: type
    :returns: Description of what the function returns.
    :rtype: type
    :raises ExceptionType: When something goes wrong.
    """
    pass
'''

Основные компоненты:
- **Параметры:** Используются директивы `:param:` и `:type:`.
- **Возвращаемое значение:** Директива `:returns:` описывает результат.
- **Тип возврата:** Директива `:rtype:` определяет тип возвращаемого значения.

Пример использования:
'''
def divide_numbers(dividend, divisor):
    """
    Деление одного числа на другое.

    :param dividend: Число, которое делят.
    :type dividend: float
    :param divisor: Число, на которое делят.
    :type divisor: float
    :returns: Результат деления.
    :rtype: float
    :raises ZeroDivisionError: Если делитель равен нулю.
    """
    if divisor == 0:
        raise ZeroDivisionError("Делитель не может быть нулевым")
    return dividend / divisor
'''

### Рекомендации по оформлению docstrings:
1. **Краткость и точность.** Докстринг должен давать точное и 
                    краткое описание функции.
                    
2. **Последовательность стилей.** Выберите один стиль (Google, NumPy, reST) и 
                    придерживайтесь его на протяжении всего проекта.
                    
3. **Документация параметров и возвращаемых значений.** Всегда документируйте 
                    аргументы и возвращаемые значения, включая их типы.
                    
4. **Исключения.** Документирование возможных исключений помогает пользователям 
                    предвидеть риски и обработать их соответствующим образом.
                    
5. **Пример использования.** Включите небольшие примеры кода, демонстрирующие 
                    применение функции.

Поддерживая хорошие практики написания docstrings, вы обеспечите вашим коллегам 
и будущим разработчикам лучшее понимание вашего кода, повысите качество 
продукта и упростите его дальнейшее развитие.
'''