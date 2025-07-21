import psycopg2 as PyPG

# ================ ШАГ №-1 =====================
# # Подключаемся к базе данных
# connectBD = PyPG.connect(
#     dbname = "IT-company",
#     user = "FaDaliAstro",
#     password = "AfyLfkbyb=(1979)",
#     host = "localhost",
#     port = 5432
# )
#
# # Общение с Базой
# cursor = connectBD.cursor()
#
# query = "SELECT * FROM customers;"
#
# cursor.execute(query)
# table = cursor.fetchall()
# print(table)
#
# --------- здесь шаг №-2 -----------
#
# # Обязательно!!! Закрываем все соединения после каждой программы.
# cursor.close()
# connectBD.close()
# ================ ШАГ №-1 ================= end

# ================ ШАГ №-2 =====================
connectBD = PyPG.connect(
    dbname = "IT-company",
    user = "FaDaliAstro",
    password = "AfyLfkbyb=(1979)",
    host = "localhost",
    port = 5432
)

# Общение с Базой
cursor = connectBD.cursor()

# ======================= query ======================
# I вариант == query ==
# query = "SELECT id, firm_name, contact_person, phone_number FROM customers;"
# I вариант == query ==
query = """
        SELECT
            projects.customer_id AS Заказчик
            ,to_char(projects.project_start, 'DD-MM-YYYY') AS Старт
            ,to_char(projects.project_end, 'DD-MM-YYYY') AS Окончание
            ,projects.title AS Проект
            FROM projects;
        """
# ======================= query ================== end

cursor.execute(query)
table = cursor.fetchall()

# === I вариант ==== ШАГ №-2 ====================
cel1 = 4
cel2 = 15
cel3 = 15
cel4 = 30

print("\nЗАКАЗЧИКИ")
print("+" + "-"*cel1 + "+" + "-"*cel2 + "+" + "-"*cel3 + "+" + "-"*cel4 + "+")
for line in table:
    print(f"|{line[0]:^{cel1}}| {line[1]:^{cel2}}| {line[2]:^{cel3}}| "
          f"{line[3]:<{cel4}} |")
    # print("+" + "-"*cel1 + "+" + "-"*cel2 + "+" + "-"*cel3 + "+" + "-"*cel4 + "+")
# === I вариант ==== ШАГ №-2 ================ end

# # === II вариант ==== ШАГ №-2 ===================
# print("\nЗАКАЗЧИКИ")
#
# for line in table:
#     for element in line:
#         print(element, end= " - ")
#     print()
# # === II вариант === ШАГ №-2 ================ end

# # === III вариант ==== ШАГ №-2 ==== выравнивание ==
# def find_column_widths(table):
#     column_widths = []
#     for row in table:
#         if len(column_widths) < len(row):
#             column_widths.extend([len(str(x)) for x in row[len(column_widths):]])
#         else:
#             for i, value in enumerate(row):
#                 column_widths[i] = max(column_widths[i], len(str(value)))
#     return column_widths
#
# column_widths = find_column_widths(table)
#
# print("\nЗАКАЗЧИКИ:")
# for line in table:
#     for idx, element in enumerate(line):
#         print(str(element).ljust(column_widths[idx]), end=" ")
#     print()
# # === III вариант ==== ШАГ №-2 ==== выравнивание == end

# ================ ШАГ №-2 ================== end

# Обязательно!!! Закрываем все соединения после каждой программы.
cursor.close()
connectBD.close()