def find_longest_line_length(input_file):
    max_length = 0  # Переменная для хранения максимальной длины

    # Открываем файл для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line_length = len(line.rstrip('\n'))  # Находим длину строки без символа новой строки
            if line_length > max_length:
                max_length = line_length  # Обновляем максимальную длину, если нужно

    return max_length

# Пример использования функции
longest_length = find_longest_line_length('input.txt')
print(f"Длина самой длинной строки: {longest_length}")
