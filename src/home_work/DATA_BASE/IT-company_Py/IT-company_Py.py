import psycopg2 as PyPG
from datetime import datetime
from collections import OrderedDict


class DBManager:
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

    def execute_query(self, query, params=None):
        # Выполнение запроса к базе данных
        conn = self._connect()  # Открытие нового соединения
        cursor = conn.cursor()  # Создание курсора
        try:
            if params:
                cursor.execute(query, params)  # Выполнение запроса с параметрами
            else:
                cursor.execute(query)  # Выполнение запроса без параметров
            conn.commit()  # Подтверждение транзакции
        finally:
            cursor.close()  # Закрытие курсора
            conn.close()    # Закрытие соединения

    def fetch_all(self, query):
        # Получение всех строк результата запроса
        conn = self._connect()  # Открытие нового соединения
        cursor = conn.cursor()  # Создание курсора
        try:
            cursor.execute(query)  # Выполнение запроса
            results = cursor.fetchall()  # Получение всех строк результата
            return results
        finally:
            cursor.close()  # Закрытие курсора
            conn.close()    # Закрытие соединения

    def create_all_tables(self):
        # Создание всех таблиц в базе данных
        tables = OrderedDict([
            ('customers', """
                CREATE TABLE IF NOT EXISTS customers (
                    id SERIAL PRIMARY KEY,
                    firm_name VARCHAR(255),
                    contact_person VARCHAR(255),
                    phone_number VARCHAR(20)
                );
            """),
            ('project_managers', """
                CREATE TABLE IF NOT EXISTS project_managers (
                    id SERIAL PRIMARY KEY,
                    birth_date DATE,
                    full_name VARCHAR(255),
                    phone_number VARCHAR(20)
                );
            """),
            ('programmers', """
                CREATE TABLE IF NOT EXISTS programmers (
                    id SERIAL PRIMARY KEY,
                    birth_date DATE,
                    full_name VARCHAR(255),
                    skill_level VARCHAR(50),
                    phone_number VARCHAR(20)
                );
            """),
            ('projects', """
                CREATE TABLE IF NOT EXISTS projects (
                    id SERIAL PRIMARY KEY,
                    customer_id INTEGER REFERENCES customers(id),
                    project_start DATE,
                    project_end DATE,
                    project_manager_id INTEGER REFERENCES project_managers(id),
                    title VARCHAR(255)
                );
            """),
            ('tasks', """
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    project_id INTEGER REFERENCES projects(id),
                    task_start TIMESTAMP,
                    task_end TIMESTAMP,
                    responsible_person_id INTEGER REFERENCES programmers(id),
                    description TEXT
                );
            """),
            ('project_programmer_link', """
                CREATE TABLE IF NOT EXISTS project_programmer_link (
                    project_id INTEGER REFERENCES projects(id),
                    programmer_id INTEGER REFERENCES programmers(id),
                    PRIMARY KEY (project_id, programmer_id)
                );
            """)
        ])

        for table_name, sql in tables.items():
            self.execute_query(sql)  # Выполнение запроса на создание таблицы


class Customer(DBManager):
    def __init__(self, db_manager):
        # Инициализация родительского класса с параметрами подключения
        super().__init__(db_manager.dbname,
                         db_manager.user,
                         db_manager.password,
                         db_manager.host,
                         db_manager.port)
        self.create_table_if_not_exists()  # Создание таблицы customers, если она не существует

    def create_table_if_not_exists(self):
        # Создание таблицы customers, если она не существует
        query = """
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            firm_name VARCHAR(255),
            contact_person VARCHAR(255),
            phone_number VARCHAR(20)
        );
        """
        self.execute_query(query)  # Выполнение запроса на создание таблицы

    def create_customer(self, firm_name, contact_person, phone_number):
        # Добавление нового заказчика в таблицу customers
        query = """INSERT INTO customers (firm_name, 
                                        contact_person, 
                                        phone_number) VALUES (%s, %s, %s);"""
        self.execute_query(query, (firm_name,
                                   contact_person,
                                   phone_number))  # Выполнение запроса

    def read_customers(self):
        # Получение всех заказчиков из таблицы customers
        query = """SELECT id, 
                            firm_name, 
                            contact_person, 
                            phone_number FROM customers;"""
        result = self.fetch_all(query)  # Получение всех строк результата

        headers = ["ID", "Фирма", "Заказчик", "Телефон"]
        widths = [len(h) for h in headers]

        for row in result:
            for i, cell in enumerate(row):
                width = len(str(cell))
                if width > widths[i]:
                    widths[i] = width

        header_line = '| '.join(header.ljust(width) for header, width in zip(headers, widths))
        separator = '-' * sum(widths) + '--' * (len(headers) - 1)

        print()
        print("ЗАКАЗЧИКИ")
        print(separator)
        print(header_line)
        print(separator)

        for row in result:
            formatted_row = '| '.join(str(cell).ljust(width) for cell, width in zip(row, widths))
            print(formatted_row)

        print(separator)

    def update_customer(self, customer_id, new_data):
        # Обновление данных заказчика в таблице customers
        query = """UPDATE customers SET firm_name=%s, contact_person=%s, phone_number=%s WHERE id=%s;"""
        self.execute_query(query, (
            new_data['firm_name'], new_data['contact_person'],
            new_data['phone_number'], customer_id
        ))

    def delete_customer(self, customer_id):
        # Удаление заказчика из таблицы customers
        query = """DELETE FROM customers WHERE id=%s;"""
        self.execute_query(query, (customer_id,))


class Project(DBManager):
    def __init__(self, db_manager):
        super().__init__(db_manager.dbname, db_manager.user,
                         db_manager.password, db_manager.host, db_manager.port)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER REFERENCES customers(id),
            project_start DATE,
            project_end DATE,
            project_manager_id INTEGER REFERENCES project_managers(id),
            title VARCHAR(255)
        );
        """
        self.execute_query(query)

    def create_project(self, customer_id, start_date, end_date, manager_id,
                       title):
        query = """INSERT INTO projects (customer_id, project_start, project_end, project_manager_id, title) VALUES (%s, %s, %s, %s, %s);"""
        self.execute_query(query, (
        customer_id, start_date, end_date, manager_id, title))

    # def read_projects(self):
    #     query = """
    #         SELECT
    #             p.id, c.firm_name, to_char(p.project_start, 'DD.MM.YYYY'), to_char(p.project_end, 'DD.MM.YYYY'),
    #             pm.full_name, p.title
    #         FROM projects p
    #         JOIN customers c ON p.customer_id = c.id
    #         LEFT JOIN project_managers pm ON p.project_manager_id = pm.id;
    #     """
    #     return self.fetch_all(query)

    def read_projects(self):
        with DBManager(self.dbname, self.user, self.password, self.host,
                       self.port) as db:
            query = """
                SELECT p.id, c.firm_name, to_char(p.project_start, 'DD.MM.YYYY'), to_char(p.project_end, 'DD.MM.YYYY'),
                       pm.full_name, p.title
                FROM projects p
                JOIN customers c ON p.customer_id = c.id
                LEFT JOIN project_managers pm ON p.project_manager_id = pm.id;
            """
            results = self.fetch_all(query)

            headers = ["ID", "Заказчик", "Дата начала", "Дата окончания",
                       "Менеджер", "Название проекта"]
            widths = [len(h) for h in headers]

            for row in results:
                for i, cell in enumerate(row):
                    width = len(str(cell))
                    if width > widths[i]:
                        widths[i] = width

            header_line = '| '.join(
                header.ljust(width) for header, width in zip(headers, widths))
            separator = '-' * sum(widths) + '--' * (len(headers) - 1)

            print()
            print("ПРОЕКТЫ")
            print(separator)
            print(header_line)
            print(separator)

            for row in results:
                formatted_row = '| '.join(
                    str(cell).ljust(width) for cell, width in zip(row, widths))
                print(formatted_row)

            print(separator)

    def update_project(self, project_id, new_data):
        query = """
            UPDATE projects SET customer_id=%s, project_start=%s, project_end=%s, project_manager_id=%s, title=%s WHERE id=%s;
        """
        self.execute_query(query, (
            new_data['customer_id'],
            new_data['start_date'],
            new_data['end_date'],
            new_data['manager_id'],
            new_data['title'],
            project_id
        ))

    def delete_project(self, project_id):
        query = """DELETE FROM projects WHERE id=%s;"""
        self.execute_query(query, (project_id,))


class ProjectManager(DBManager):
    def __init__(self, db_manager):
        super().__init__(db_manager.dbname, db_manager.user,
                         db_manager.password, db_manager.host, db_manager.port)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS project_managers (
            id SERIAL PRIMARY KEY,
            birth_date DATE,
            full_name VARCHAR(255),
            phone_number VARCHAR(20)
        );
        """
        self.execute_query(query)

    def create_manager(self, birth_date, full_name, phone_number):
        query = """INSERT INTO project_managers (birth_date, full_name, phone_number) VALUES (%s, %s, %s);"""
        self.execute_query(query, (birth_date, full_name, phone_number))

    def read_managers(self):
        with DBManager(self.dbname, self.user, self.password, self.host,
                       self.port) as db:
            query = """SELECT id, to_char(birth_date, 'DD.MM.YYYY'), full_name, phone_number FROM project_managers;"""
            results = self.fetch_all(query)

            headers = ["ID", "Дата рождения", "ФИО", "Телефон"]
            widths = [len(h) for h in headers]

            for row in results:
                for i, cell in enumerate(row):
                    width = len(str(cell))
                    if width > widths[i]:
                        widths[i] = width

            header_line = '| '.join(
                header.ljust(width) for header, width in zip(headers, widths))
            separator = '-' * sum(widths) + '--' * (len(headers) - 1)

            print()
            print("МЕНЕДЖЕРЫ")
            print(separator)
            print(header_line)
            print(separator)

            for row in results:
                formatted_row = '| '.join(
                    str(cell).ljust(width) for cell, width in zip(row, widths))
                print(formatted_row)

            print(separator)

    def update_manager(self, manager_id, new_data):
        query = """UPDATE project_managers SET birth_date=%s, full_name=%s, phone_number=%s WHERE id=%s;"""
        self.execute_query(query, (
        new_data['birth_date'], new_data['full_name'],
        new_data['phone_number'], manager_id))

    def delete_manager(self, manager_id):
        query = """DELETE FROM project_managers WHERE id=%s;"""
        self.execute_query(query, (manager_id,))


class Task(DBManager):
    def __init__(self, db_manager):
        super().__init__(db_manager.dbname, db_manager.user,
                         db_manager.password, db_manager.host, db_manager.port)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            project_id INTEGER REFERENCES projects(id),
            task_start TIMESTAMP,
            task_end TIMESTAMP,
            responsible_person_id INTEGER REFERENCES programmers(id),
            description TEXT
        );
        """
        self.execute_query(query)

    def create_task(self, project_id, start_time, end_time, programmer_id,
                    description):
        query = """INSERT INTO tasks (project_id, task_start, task_end, responsible_person_id, description) VALUES (%s, %s, %s, %s, %s);"""
        self.execute_query(query, (
        project_id, start_time, end_time, programmer_id, description))

    def read_tasks(self):
        with DBManager(self.dbname, self.user, self.password, self.host,
                       self.port) as db:
            query = """
                SELECT t.id, p.title, to_char(t.task_start, 'DD.MM.YYYY HH24:MI:SS'), to_char(t.task_end, 'DD.MM.YYYY HH24:MI:SS'),
                       pr.full_name, t.description
                FROM tasks t
                JOIN projects p ON t.project_id = p.id
                JOIN programmers pr ON t.responsible_person_id = pr.id;
            """
            results = self.fetch_all(query)

            headers = ["ID", "Задача", "Дата начала", "Дата окончания",
                       "Программист", "Описание"]
            widths = [len(h) for h in headers]

            for row in results:
                for i, cell in enumerate(row):
                    width = len(str(cell))
                    if width > widths[i]:
                        widths[i] = width

            header_line = '| '.join(
                header.ljust(width) for header, width in zip(headers, widths))
            separator = '-' * sum(widths) + '--' * (len(headers) - 1)

            print()
            print("ЗАДАЧИ")
            print(separator)
            print(header_line)
            print(separator)

            for row in results:
                formatted_row = '| '.join(
                    str(cell).ljust(width) for cell, width in zip(row, widths))
                print(formatted_row)

            print(separator)

    def update_task(self, task_id, new_data):
        query = """
            UPDATE tasks SET project_id=%s, task_start=%s, task_end=%s, responsible_person_id=%s, description=%s WHERE id=%s;
        """
        self.execute_query(query, (
            new_data['project_id'],
            new_data['start_time'],
            new_data['end_time'],
            new_data['programmer_id'],
            new_data['description'],
            task_id
        ))

    def delete_task(self, task_id):
        query = """DELETE FROM tasks WHERE id=%s;"""
        self.execute_query(query, (task_id,))


class Programmer(DBManager):
    def __init__(self, db_manager):
        super().__init__(db_manager.dbname, db_manager.user,
                         db_manager.password, db_manager.host, db_manager.port)
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS programmers (
            id SERIAL PRIMARY KEY,
            birth_date DATE,
            full_name VARCHAR(255),
            skill_level VARCHAR(50),
            phone_number VARCHAR(20)
        );
        """
        self.execute_query(query)

    def create_programmer(self, birth_date, full_name, skill_level,
                          phone_number):
        query = """INSERT INTO programmers (birth_date, full_name, skill_level, phone_number) VALUES (%s, %s, %s, %s);"""
        self.execute_query(query,
                           (birth_date, full_name, skill_level, phone_number))

    def read_programmers(self):
        with DBManager(self.dbname, self.user, self.password, self.host,
                       self.port) as db:
            query = """SELECT id, to_char(birth_date, 'DD.MM.YYYY'), full_name, skill_level, phone_number FROM programmers;"""
            results = self.fetch_all(query)

            headers = ["ID", "Дата рождения", "ФИО", "Уровен",
                       "Телефон"]
            widths = [len(h) for h in headers]

            for row in results:
                for i, cell in enumerate(row):
                    width = len(str(cell))
                    if width > widths[i]:
                        widths[i] = width

            header_line = '| '.join(
                header.ljust(width) for header, width in zip(headers, widths))
            separator = '-' * sum(widths) + '--' * (len(headers) - 1)

            print()
            print("ПРОГРАММИСТЫ")
            print(separator)
            print(header_line)
            print(separator)

            for row in results:
                formatted_row = '| '.join(
                    str(cell).ljust(width) for cell, width in zip(row, widths))
                print(formatted_row)

            print(separator)

    def update_programmer(self, programmer_id, new_data):
        query = """UPDATE programmers SET birth_date=%s, full_name=%s, skill_level=%s, phone_number=%s WHERE id=%s;"""
        self.execute_query(query, (
        new_data['birth_date'], new_data['full_name'], new_data['skill_level'],
        new_data['phone_number'], programmer_id))

    def delete_programmer(self, programmer_id):
        query = """DELETE FROM programmers WHERE id=%s;"""
        self.execute_query(query, (programmer_id,))

# ================ МЕНЮ ====================

def show_menu():
    while True:
        print("\nМеню управления базой данных IT-компании:")
        print("1. Управление заказчиками")
        print("2. Управление проектами")
        print("3. Управление менеджерами проектов")
        print("4. Управление задачами")
        print("5. Управление программистами")
        print("0. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            manage_customers()
        elif choice == '2':
            manage_projects()
        elif choice == '3':
            manage_project_managers()
        elif choice == '4':
            manage_tasks()
        elif choice == '5':
            manage_programmers()
        else:
            print("Недопустимый выбор. Выберите пункт из меню.")


def manage_customers():
    while True:
        print("\nУправление заказчиками:")
        print("1. Создать нового заказчика")
        print("2. Просмотреть всех заказчиков")
        print("3. Обновить данные заказчика")
        print("4. Удалить заказчика")
        print("0. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            firm_name = input("Название фирмы : ")
            contact_person = input("Контактное лицо: ")
            phone_number = input("Телефон        : ")
            customer.create_customer(firm_name, contact_person, phone_number)
            print("Заказчик успешно создан!")
        elif choice == '2':
            customers = customer.read_customers()
            print(customers)
        elif choice == '3':
            customer_id = int(input("ID заказчика для обновления: "))
            firm_name = input("Новое название фирмы       : ")
            contact_person = input("Новое контактное лицо      : ")
            phone_number = input("Новый телефон              : ")
            customer.update_customer(customer_id, {'firm_name': firm_name,
                                                   'contact_person': contact_person,
                                                   'phone_number': phone_number})
            print("Данные заказчика обновлены!")
        elif choice == '4':
            customer_id = int(input("ID заказчика для удаления: "))
            customer.delete_customer(customer_id)
            print("Заказчик удален!")
        else:
            print("Недопустимый выбор. Выберите действие из меню.")


def manage_projects():
    while True:
        print("\nУправление проектами:")
        print("1. Создать новый проект")
        print("2. Просмотреть все проекты")
        print("3. Обновить данные проекта")
        print("4. Удалить проект")
        print("0. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            customer_id = int(input("ID заказчика               : "))
            start_date = input("Дата старта (гггг-мм-дд)   : ")
            end_date = input("Дата окончания (гггг-мм-дд): ")
            manager_id = int(input("ID менеджера проекта       : "))
            title = input("Название проекта           : ")
            project.create_project(customer_id, start_date, end_date,
                                   manager_id, title)
            print("Проект успешно создан!")
        elif choice == '2':
            projects = project.read_projects()
            print(projects)
        elif choice == '3':
            project_id = int(input("ID проекта для обновления        : "))
            customer_id = int(input("Новый ID заказчика               : "))
            start_date = input("Новая дата старта (гггг-мм-дд)   : ")
            end_date = input("Новая дата окончания (гггг-мм-дд): ")
            manager_id = int(input("Новый ID менеджера проекта       : "))
            title = input("Новое название проекта           : ")
            project.update_project(project_id, {'customer_id': customer_id,
                                                'start_date': start_date,
                                                'end_date': end_date,
                                                'manager_id': manager_id,
                                                'title': title})
            print("Данные проекта обновлены!")
        elif choice == '4':
            project_id = int(input("ID проекта для удаления: "))
            project.delete_project(project_id)
            print("Проект удален!")
        else:
            print("Недопустимый выбор. Выберите действие из меню.")


def manage_project_managers():
    while True:
        print("\nУправление менеджерами проектов:")
        print("1. Создать нового менеджера")
        print("2. Просмотреть всех менеджеров")
        print("3. Обновить данные менеджера")
        print("4. Удалить менеджера")
        print("0. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            birth_date = input("Дата рождения (гггг-мм-дд): ")
            full_name = input("ФИО                       : ")
            phone_number = input("Телефон                   : ")
            manager.create_manager(birth_date, full_name, phone_number)
            print("Менеджер успешно создан!")
        elif choice == '2':
            managers = manager.read_managers()
            print(managers)
        elif choice == '3':
            manager_id = int(input("ID менеджера для обновления     : "))
            birth_date = input("Новая дата рождения (гггг-мм-дд): ")
            full_name = input("Новое ФИО                       : ")
            phone_number = input("Новый телефон                   : ")
            manager.update_manager(manager_id, {'birth_date': birth_date,
                                                'full_name': full_name,
                                                'phone_number': phone_number})
            print("Данные менеджера обновлены!")
        elif choice == '4':
            manager_id = int(input("ID менеджера для удаления: "))
            manager.delete_manager(manager_id)
            print("Менеджер удален!")
        else:
            print("Недопустимый выбор. Выберите действие из меню.")


def manage_tasks():
    while True:
        print("\nУправление задачами:")
        print("1. Создать новую задачу")
        print("2. Просмотреть все задачи")
        print("3. Обновить данные задачи")
        print("4. Удалить задачу")
        print("0. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            project_id = int(input("ID проекта                        : "))
            start_time = input("Время старта (гггг-мм-дд чч:мм)   : ")
            end_time = input("Время окончания (гггг-мм-дд чч:мм): ")
            programmer_id = int(input("ID программиста-исполнителя       : "))
            description = input("Описание задачи                   : ")
            task.create_task(project_id, start_time, end_time, programmer_id,
                             description)
            print("Задача успешно создана!")
        elif choice == '2':
            tasks = task.read_tasks()
            print(tasks)
        elif choice == '3':
            task_id = int(input("ID задачи для обновления                : "))
            project_id = int(input("Новый ID проекта                        : "))
            start_time = input("Новое время старта (гггг-мм-дд чч:мм)   : ")
            end_time = input("Новое время окончания (гггг-мм-дд чч:мм): ")
            programmer_id = int(input("Новый ID программиста-исполнителя       : "))
            description = input("Новое описание задачи                   : ")
            task.update_task(task_id, {'project_id': project_id,
                                       'start_time': start_time,
                                       'end_time': end_time,
                                       'programmer_id': programmer_id,
                                       'description': description})
            print("Данные задачи обновлены!")
        elif choice == '4':
            task_id = int(input("ID задачи для удаления: "))
            task.delete_task(task_id)
            print("Задача удалена!")
        else:
            print("Недопустимый выбор. Выберите действие из меню.")


def manage_programmers():
    while True:
        print("\nУправление программистами:")
        print("1. Создать нового программиста")
        print("2. Просмотреть всех программистов")
        print("3. Обновить данные программиста")
        print("4. Удалить программиста")
        print("0. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            birth_date = input("Дата рождения (гггг-мм-дд): ")
            full_name = input("ФИО                       : ")
            skill_level = input("Уровень квалификации      : ")
            phone_number = input("Телефон                   : ")
            programmer.create_programmer(birth_date, full_name, skill_level,
                                         phone_number)
            print("Программист успешно создан!")
        elif choice == '2':
            programmers = programmer.read_programmers()
            print(programmers)
        elif choice == '3':
            programmer_id = int(input("ID программиста для обновления  : "))
            birth_date = input( "Новая дата рождения (гггг-мм-дд): ")
            full_name = input( "Новое ФИО                       : ")
            skill_level = input("Новый уровень квалификации      : ")
            phone_number = input("Новый телефон                   : ")
            programmer.update_programmer(programmer_id,
                                         {'birth_date': birth_date,
                                          'full_name': full_name,
                                          'skill_level': skill_level,
                                          'phone_number': phone_number})
            print("Данные программиста обновлены!")
        elif choice == '4':
            programmer_id = int(input("ID программиста для удаления: "))
            programmer.delete_programmer(programmer_id)
            print("Программист удален!")
        else:
            print("Недопустимый выбор. Выберите действие из меню.")

# ================ МЕНЮ ================ end

def main():
    try:
        db = DBManager('it_company_py', 'postgres', 'AfyLfkbyb=(1979)')
        db.create_all_tables()  # Явно создаем все таблицы

        global customer, project, manager, task, programmer
        customer = Customer(db)
        project = Project(db)
        manager = ProjectManager(db)
        task = Task(db)
        programmer = Programmer(db)

        show_menu()

    except Exception as e:
        print(f"Возникла ошибка: {e}")
    finally:
        if 'db' in locals() and db is not None:
            db.close()


if __name__ == '__main__':
    main()