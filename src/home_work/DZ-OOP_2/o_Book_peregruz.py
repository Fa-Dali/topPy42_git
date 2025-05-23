class Book:
    logo = "Читай Город"
    indastry = "Литература"

    def __init__(self,
                 name_book = '',
                 release = 0,
                 publisher='',
                 genre='',
                 author='',
                 price = 0):
        self.name_book = name_book
        self.realise = release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def user_choice(self):
        print()
        print(f"======{Book.logo:^13}=================")
        self.name_book =     input("введите название книги       : ")
        try:
            self.realise = int(input("введите год выпуска          : "))
        except:
            print("Вы должны указать число")
        self.publisher = input("введите издателя             : ")
        self.genre     = input("введите жанр книги           : ")
        self.author    = input("введите автора книги         : ")
        try:
            self.price     = int(input("введите стоимость            : "))
        except:
            print("Вы должны указать число")

    def output_data(self, mode = ''):

        a_print = f"====={Book.indastry:^16}==================="

        if mode.lower() == '1':  # Режим сокращения
            print(a_print)
            print(f"Книга: {self.name_book}\n"
                  f"Год выпуска: {self.release}\n"
                  f"Цена: {self.price} р.")
            print("=" * len(a_print))

        print()
        print(f"======{Book.logo:^13}=================")
        print(f"Книга           : {self.name_book}")
        print(f"Год выпуска     : {self.realise} г.")
        print(f"Издатель        : {self.publisher}")
        print(f"Жанр            : {self.genre}")
        print(f"Автор           : {self.author}")
        print(f"Цена            : {self.price} р.")
        print(f"=================================")

    def get_name_book(self):
        return self.name_book

    def get_realise(self):
        return self.realise

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

def menu_logic():
    book = Book()
    book.user_choice()
    while True:
        print("----------------------------")
        print("Какой формат вывода выбрать:")
        print("1     : Сокращённый отчет")
        print("2     : Полный отчет")
        print("Enter : Выход")
        print("----------------------------")
        format_choice = input().strip().lower()
        if format_choice == '':
            break
        else:
            book.output_data(format_choice)

if __name__ == "__main__":
    menu_logic()