def remove_last_line(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # Читаем все строки

    lines = lines[:-1]

    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(lines)

remove_last_line('input.txt', 'output.txt')
