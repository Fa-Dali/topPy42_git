import psycopg2 as PyPG

# Соединение с базой данных
connectDB = PyPG.connect(
    dbname="postgres",
    user="FaDaliAstro",
    password="AfyLfkbyb=(1979)",
    host="localhost",
    port=5432
)


def connect_to_database():
    """ Функция подключения к БД """
    connectDB = PyPG.connect(
        dbname="postgres",
        user="FaDaliAstro",
        password="AfyLfkbyb=(1979)",
        host="localhost",
        port=5432
    )
    return connectDB


def create_table(name_table: str, title_values: str, connect_db):
    """ Создание таблицы """
    cursor = connect_db.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {name_table} ({title_values});"
    cursor.execute(query)
    # connect_db.commit() — лучше перенести commit ниже, после всех операций
    cursor.close()


def add_values(name_table: str, title_values: str, values: list, connect_db):
    """ Добавление значений в таблицу """
    cursor = connect_db.cursor()

    # Формирование строки значений
    values_str = ", ".join([f"('{val[0]}', {val[1]})" for val in values])

    query = f"INSERT INTO {name_table} ({title_values}) VALUES {values_str};"
    cursor.execute(query)
    # connect_db.commit() — перенесён ниже
    cursor.close()


def get_table(name_table: str, connect_db):
    """ Получение содержимого таблицы """
    cursor = connect_db.cursor()
    query = f"SELECT * FROM {name_table};"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


# Основная логика программы
if __name__ == "__main__":
    connectDB = connect_to_database()

    # Структура таблицы
    table_create_values_title = (
        "id uuid DEFAULT gen_random_uuid(),"
        "name text NOT NULL,"
        "age integer,"
        "PRIMARY KEY(id)"
    )

    # Название таблицы
    name_table = "example_table"

    # Создаем таблицу
    create_table(name_table, table_create_values_title, connectDB)

    # Добавляем данные
    data = [
        ("Вася", 10),
        ("Маша", 12),
        ("Оля", 15)
    ]
    add_values(name_table, "name, age", data, connectDB)

    # Подтверждение изменений
    connectDB.commit()

    # Читаем содержимое таблицы
    lst = get_table(name_table, connectDB)
    for row in lst:
        print(row)

    # Закрываем соединение
    connectDB.close()