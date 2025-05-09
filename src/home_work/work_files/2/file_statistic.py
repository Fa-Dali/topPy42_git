# Функция для подсчёта статистики в файле
def count_statistics(input_file, output_file):
    vowels = "АЕЁИОУЫЭЮЯаеёиоуыэюя"  # Гласные буквы
    consonants = "БВГДЁЖЗЙКЛМНОПРСТФХЦЧШЩбвгдёжзйклмнопрстфхцчшщ"  # Согласные буквы
    digits = "0123456789"  # Цифры

    num_chars = 0
    num_lines = 0
    num_vowels = 0
    num_consonants = 0
    num_digits = 0

    # Открываем файл для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            num_lines += 1  # Считаем строки
            num_chars += len(line)  # Считаем количество символов

            for char in line:
                if char in vowels:
                    num_vowels += 1  # Считаем гласные
                elif char in consonants:
                    num_consonants += 1  # Считаем согласные
                elif char in digits:
                    num_digits += 1  # Считаем цифры

    # Записываем статистику в новый файл
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(f"Количество символов: {num_chars}\n")
        output.write(f"Количество строк: {num_lines}\n")
        output.write(f"Количество гласных букв: {num_vowels}\n")
        output.write(f"Количество согласных букв: {num_consonants}\n")
        output.write(f"Количество цифр: {num_digits}\n")

# Пример использования функции
count_statistics('input.txt', 'statistics.txt')
