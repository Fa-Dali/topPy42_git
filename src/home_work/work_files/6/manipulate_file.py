def replace_word_in_file(input_file, target_word, replacement_word):

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Заменяем все вхождения целевого слова на новое слово
    new_content = content.replace(target_word, replacement_word)

    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

input_file = 'input.txt'
target_word = input("Введите слово для замены: ")
replacement_word = input("Введите новое слово: ")

replace_word_in_file(input_file, target_word, replacement_word)
print(f"Слово '{target_word}' заменено на '{replacement_word}' в файле '{input_file}'.")
