'''
Задание
Пользователь с клавиатуры вводит путь к существующей директории и слово для
поиска.

После чего запускаются два потока.
-- Первый должен найти файлы, содержащие искомое слово и
   слить их содержимое в один файл.
-- Второй поток ожидает завершения работы первого потока.

После чего проводит вырезание всех запрещенных слов
(список этих слов нужно считать из файла с запрещенными словами)
из полученного файла.

На экран необходимо отобразить статистику выполненных операций.
'''

import os
import re
import threading
from collections import Counter

# Читаем запрещённые слова из файла
def read_banned_words(filename):
    with open(filename, encoding='utf-8', errors='ignore') as f:
        banned_words = set(line.strip().lower() for line in f.readlines())
    return banned_words

# Ищем файлы, содержащие нужное слово, и сливаем их содержимое
def find_and_merge_files(directory, search_word, result_filename):
    found_files = []
    merged_content = ""

    # Ищем файлы с нужным словом
    for root, _, files in os.walk(directory):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            try:
                with open(full_path, encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if search_word.lower() in content.lower():
                        found_files.append(full_path)
                        merged_content += content + "\n\n"
            except UnicodeDecodeError:
                continue  # Пропускаем некорректно закодированные файлы

    # Сохраняем контент в итоговом файле
    with open(result_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(merged_content)

    return found_files

# Удаляем запрещённые слова из итогового файла
def remove_banned_words(banned_words, result_filename):
    with open(result_filename, 'r+', encoding='utf-8') as f:
        text = f.read()
        words_to_remove = Counter()
        for word in banned_words:
            count = len(re.findall(r'\b' + re.escape(word) + r'\b', text, flags=re.IGNORECASE))
            if count > 0:
                words_to_remove[word] += count
                text = re.sub(r'\b' + re.escape(word) + r'\b', '', text, flags=re.IGNORECASE)
        f.seek(0)
        f.truncate()
        f.write(text)
    return dict(words_to_remove)

# Основная программа
if __name__ == '__main__':
    # Получаем входные данные от пользователя
    directory = input("Введите путь к директории: ")
    search_word = input("Введите слово для поиска: ")
    banned_words_file = input("Введите путь к файлу с запрещёнными словами: ")

    # Загружаем запрещённые слова
    banned_words = read_banned_words(banned_words_file)

    # Имя выходного файла
    result_filename = "merged_result.txt"

    # Создаём поток для поиска и объединения файлов
    thread_find = threading.Thread(
        target=find_and_merge_files,
        args=(directory, search_word, result_filename),
        daemon=True
    )

    # Создаём поток для удаления запрещённых слов
    thread_clean = threading.Thread(
        target=lambda: remove_banned_words(banned_words, result_filename),
        daemon=True
    )

    # Запускаем поток поиска и ожидания его завершения
    thread_find.start()
    thread_find.join()

    # Начинаем удаление запрещённых слов
    removed_words = thread_clean.run()

    # Показываем статистику
    print(f"Обработано файлов: {len(find_and_merge_files(directory, search_word, result_filename))}")
    print(f"Удалено слов:")
    for word, count in removed_words.items():
        print(f"- '{word}' встречалось {count} раз")