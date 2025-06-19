import json

class CountryCapitalManager:
    def __init__(self, filename='countries.json'):
        """
        Конструктор класса инициализирует переменные и загружает данные из файла.
        :param filename: Имя файла для хранения данных
        """
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        """Частная функция для загрузки данных из файла"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {} # Если файл отсутствует, начинаем с пустого словаря.

    def _save_data(self):
        """Частная функция для сохранения данных в файл"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_country(self, country, capital):
        """
        Добавляет новую страну и ее столицу в хранилище
        :param country: название страны
        :param capital: Название столицы
        """
        self.data[country] = capital
        self._save_data()

    def remove_country(self, country):
        """
        Удоляет страну и ее столицу из хранилища.
        :param ciuntry: Название страны
        """
        if country in self.data:
            print(f"Удаляем Х-{country}-Х")
            del self.data[country]
            self._save_data()
        else:
            raise KeyError(f"Страна '{country}' не существует.")

    def search_capital(self, country):
        """
        Возвращает столицу указанной страны.
        :param country: Название страны
        :return: Название столицы или сообщение об ошибке
        """
        return self.data.get(country, f"Информация о {country} не найдена")

    def update_capital(self, country, new_capital):
        """
        Изменяем столицу выбранной страны.
        :param country: Название страны
        :param new_capital: Новое название столиуы
        """
        if country in self.data:
            self.data[country] = new_capital
            self._save_data()
        else:
            raise KeyError(f"Страна '{country}' не существует.")

manager = CountryCapitalManager()

manager.add_country("Россия", "Москва")
manager.add_country("Франция", "Париж")

# Поиск данных
print(manager.search_capital("Россия"))   # Москва
print(manager.search_capital("Германия")) # Информация не найдена

# Обновляем данные
manager.update_capital("Франция", "Марсель")
print(manager.search_capital("Франция"))  # Марсель

# Удаляем страну
manager.remove_country("Россия")
print(manager.search_capital("Россия"))   # Информация не найдена