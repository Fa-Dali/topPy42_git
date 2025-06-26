import json

from numpy.random import choice


class MusicDatabase:
    def __init__(self, filename="music.json"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        '''Загружает данные из JSON-файла'''
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        '''Сохраняет данные в JSON-файл'''
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
        print("Данные сохранены успешно!")

    def add_group_or_album(self, group_name, album=None):
        '''Добавляет новую группу или альбом'''
        if group_name in self.data:
            if album is not None:
                self.data[group_name].append(album)
        else:
            self.data[group_name] = [] if album is None else [album]
        print(f"{group_name}: {self.data.get(group_name)}")

    def remove_group_or_album(self, group_name, album=None):
        '''Удоляет группу или альбом'''
        if group_name in self.data:
            if album is None or len(self.data[group_name]) <= 1:
                del self.data[group_name]
                print(f"Удалена группа '{group_name}'")
            elif album in self.data[group_name]:
                self.data[group_name].remove(album)
                print(f"Удалён альбом '{album}' из группы '{group_name}'")
            else:
                print("Альбом не найден.")
        else:
            print("Группа не найдена.")

    def edit_album(self, group_name, old_album, new_album):
        '''Редактирует существующий альбом'''
        if group_name in self.data and old_album in self.data[group_name]:
            index = self.data[group_name].index(old_album)
            self.data[group_name].index(old_album)
            print(f"Обновлён альбом '{old_album}' на '{new_album}' в группе "
                  f"'{group_name}'.")
        else:
            print("Группа или альбом не найден.")

    def show_all(self):
        '''Показывает все имеющиеся данные'''
        for group, album in self.data.items():
            print(f"{group}: {album}")

if __name__ == "__main__":
    db = MusicDatabase()

    while True:
        print("\nМеню:")
        print("1. Добавить группу или альбом")
        print("2. Удалить группу или альбом")
        print("3. Редактировать альбом.")
        print("4. Показать данные.")
        print("5. Сохранить данные.")
        print("6. Выход.")

        choice = input("Ваш выбор:")

        if choice == '1':
            group_name = input("Введите название группы: ").strip()
            album = (input("Введите название альбома (оставьте пустым, "
                          "если хотите добавить только группу: ").strip() or
                     None)
            db.add_group_or_album(group_name, album)

        elif choice == '2':
            group_name = input("Введите название группы: ").strip()
            album = input("Введите название альбома (оставьте пустым, "
                          "если хотите удалить всю группу): ").strip() or None
            db.remove_group_or_album(group_name, album)

        elif choice == '3':
            group_name = input("Введите название группы: ").strip()
            old_album = input("Введите старый альбом: ").strip()
            new_album = input("Введите новый альбом: ").strip()
            db.edit_album(group_name, old_album, new_album)

        elif choice == '4':
            db.show_all()

        elif choice == '5':
            db.save_data()

        elif choice == '6':
            break

        else:
            print("Некорректный ввод.")