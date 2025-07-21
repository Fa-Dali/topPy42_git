# Модуль для работы с Базой Данных PostgreSQL

import psycopg2 as PyPG

# Класс для управления ролями в PostgreSQL
class RoleManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        # Инициализация параметров подключения к базе данных
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def _connect(self):
        # Создание нового соединения с базой данных
        return PyPG.connect(dbname=self.dbname, user=self.user,
                           password=self.password, host=self.host, port=self.port)

    def execute_query(self, query):
        # Выполнение запроса к базе данных
        conn = self._connect()  # Открытие нового соединения
        cursor = conn.cursor()  # Создание курсора
        try:
            cursor.execute(query)  # Выполнение запроса
            conn.commit()  # Подтверждение транзакции
        finally:
            cursor.close()  # Закрытие курсора
            conn.close()    # Закрытие соединения

    def create_role(self, role_name, password, **options):
        """
        Создает новую роль с указанными привилегиями.

        :param role_name: Имя роли
        :param password: Пароль для роли
        :param options: Дополнительные опции (SUPERUSER, CREATEDB, CREATEROLE, INHERIT, LOGIN, BYPASSRLS, CONNECTION LIMIT)
        """
        # Формирование строки с опциями
        options_str = []
        if options.get('SUPERUSER'):
            options_str.append('SUPERUSER')
        if options.get('CREATEDB'):
            options_str.append('CREATEDB')
        if options.get('CREATEROLE'):
            options_str.append('CREATEROLE')
        if options.get('INHERIT'):
            options_str.append('INHERIT')
        if options.get('LOGIN'):
            options_str.append('LOGIN')
        if options.get('BYPASSRLS'):
            options_str.append('BYPASSRLS')
        if 'CONNECTION LIMIT' in options:
            options_str.append(f'CONNECTION LIMIT {options["CONNECTION LIMIT"]}')

        options_str = ' '.join(options_str)
        # Формирование запроса на создание роли
        query = f"CREATE ROLE {role_name} WITH {options_str} PASSWORD '{password}';"
        self.execute_query(query)  # Выполнение запроса

    def grant_privileges(self, role_name, privileges):
        """
        Предоставляет привилегии роли.

        :param role_name: Имя роли
        :param privileges: Список привилегий (например, ['CREATEDB', 'CREATEROLE'])
        """
        # Формирование строки с привилегиями
        privileges_str = ', '.join(privileges)
        # Формирование запроса на предоставление привилегий
        query = f"GRANT {privileges_str} TO {role_name};"
        self.execute_query(query)  # Выполнение запроса

# Пример использования
if __name__ == '__main__':
    # Подключение к базе данных
    role_manager = RoleManager('your_database', 'your_user', 'your_password')

    # Выбор роли пользователем
    print("Выберите роль:")
    print("1. Обычный пользователь")
    print("2. Администратор")
    print("3. Разработчик")
    choice = input("Введите номер роли: ")

    # Ввод имени и пароля
    role_name = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    # Создание роли в зависимости от выбора пользователя
    if choice == '1':
        # Обычный пользователь
        role_manager.create_role(role_name, password, LOGIN=True)
    elif choice == '2':
        # Администратор
        role_manager.create_role(role_name, password, SUPERUSER=True, LOGIN=True)
    elif choice == '3':
        # Разработчик
        role_manager.create_role(role_name, password, CREATEDB=True, CREATEROLE=True, LOGIN=True)
    else:
        print("Недопустимый выбор роли.")