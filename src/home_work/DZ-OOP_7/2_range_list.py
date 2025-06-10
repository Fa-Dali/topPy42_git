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

# Функция для поиска простых чисел в заданном диапазоне
@timer_decorator
def find_primes(start, end):
    primes = []  # пустой список для хранения простых чисел
    for num in range(start, end + 1):
        if num < 2:
            continue  # пропускаем числа меньше 2
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Запрашиваем границы диапазона у пользователя
lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))

# Находим простые числа в заданном диапазоне
primes_list = find_primes(lower_bound, upper_bound)

# Печать найденных простых чисел
print("Простые числа в заданном диапазоне:")
for i, prime in enumerate(primes_list):
    print(prime, end=" ")
    if (i + 1) % 10 == 0:
        print("\n")

if primes_list:
    print("\nВсего найдено простых чисел:", len(primes_list))
else:
    print("\nПростых чисел в данном диапазоне не обнаружено.")