import time

# Декоратор для замера времени выполнения функции
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # фиксируем начальное время
        result = func(*args, **kwargs)  # выполняем основную функцию
        end_time = time.time()  # фиксируем конечное время
        execution_time = end_time - start_time  # считаем разницу
        print(f"Время выполнения: {execution_time:.6f} секунд")
        return result
    return wrapper

# Функция для поиска простых чисел до указанного предела
@timer_decorator
def find_primes_up_to(limit):
    primes = []  # пустой список для хранения простых чисел
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Вызов функции с лимитом 1000
primes_list = find_primes_up_to(1000)

# Печать найденных простых чисел
print("Список простых чисел до 1000:")
print(primes_list)

