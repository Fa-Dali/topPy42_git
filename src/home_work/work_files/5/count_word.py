def count_word_occurrences(input_file, target_word):
    count = 0  # Счётчик для слова

    # Открываем файл для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Разбиваем строку на слова и считаем вхождения целевого слова
            words = line.split()
            count += words.count(target_word)

    return count

# Пример использования функции
input_file = 'input.txt'
target_word = input("Введите слово для поиска: ")

occurrences = count_word_occurrences(input_file, target_word)
print(f"Слово '{target_word}' встречается {occurrences} раз(а) в файле '{input_file}'.")
