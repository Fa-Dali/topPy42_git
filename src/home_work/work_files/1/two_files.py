# Открываем оба файла для чтения
with open('file1.txt', 'r', encoding='utf-8') as file1:
    lines1 = file1.readlines()

with open('file2.txt', 'r', encoding='utf-8') as file2:
    lines2 = file2.readlines()

# Приводим строки к виду без лишних пробелов и символов новой строки
cleaned_lines1 = []
for line in lines1:
    cleaned_lines1.append(line.strip())

cleaned_lines2 = []
for line in lines2:
    cleaned_lines2.append(line.strip())

# Устанавливаем минимальное количество строк для перебора
min_lines = min(len(lines1), len(lines2))

# Проверяем строки на совпадение
for i in range(min_lines):
    if lines1[i] != lines2[i]:
        print(f"Несовпадающая строка из file1.txt: '{lines1[i]}'")
        print(f"Несовпадающая строка из file2.txt: '{lines2[i]}'")

# Если один файл длиннее другого, выводим остальные строки
if len(lines1) > len(lines2):
    for i in range(len(lines2), len(lines1)):
        print(f"Дополнительная строка из file1.txt: '{lines1[i]}'")
elif len(lines2) > len(lines1):
    for i in range(len(lines1), len(lines2)):
        print(f"Дополнительная строка из file2.txt: '{lines2[i]}'")
