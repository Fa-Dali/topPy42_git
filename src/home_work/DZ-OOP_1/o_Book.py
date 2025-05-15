class Book:
    def __init__(self,
                 name_book = '',
                 release = 0,
                 publisher='',
                 genre='',
                 author='',
                 price = 0):

        self.name_book = name_book
        self.realise   = release
        self.publisher = publisher
        self.genre     = genre
        self.author    = author
        self.price     = price

    def user_choice(self):
        self.name_book =     input("введите название книги       : ")
        self.realise   =     input("введите год выпуска          : ")
        self.publisher =     input("введите издателя             : ")
        self.genre     =     input("введите жанр книги           : ")
        self.author    =     input("введите автора книги         : ")
        self.price     = int(input("введите стоимость            : "))

    def output_data(self):
        print(f"=================================")
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

if __name__ == "__main__":
    book = Book()
    book.user_choice()
    book.output_data()