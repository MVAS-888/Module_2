class Book:
    def __init__(self, author: str, title: str, year: int, genre: str):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Book({self.author!r}, {self.title!r}, {self.year!r}, {self.genre!r})"

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year} ({self.genre})"


# Приклад використання
book1 = Book("Джордж Орвелл", "1984", 1949, "Антиутопія")
book2 = Book("Френк Герберт", "Дюна", 1965, "Наукова фантастика")
book3 = Book("Марк Твен", "Пригоди Тома Сойєра", 1876, "Пригоди")

print(book1)
print(repr(book2))
