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


class Review:
    def __init__(self, reviewer: str, content: str):
        self.reviewer = reviewer
        self.content = content

    def __str__(self):
        return f"{self.reviewer}: {self.content}"


class BookWithReviews(Book):
    def __init__(self, author: str, title: str, year: int, genre: str):
        super().__init__(author, title, year, genre)
        self.reviews = []

    def add_review(self, reviewer: str, content: str):
        review = Review(reviewer, content)
        self.reviews.append(review)

    def __str__(self):
        book_info = super().__str__()
        reviews_info = "\n".join(str(review) for review in self.reviews)
        return f"{book_info}\nReviews:\n{reviews_info if self.reviews else 'No reviews yet.'}"


# Приклад використання
book_with_reviews = BookWithReviews("Френк Герберт", "Дюна", 1965, "Наукова фантастика")
book_with_reviews.add_review("Ольга", "Шедевр!")
book_with_reviews.add_review("Іван", "Цікаво, але складно читати.")
print(book_with_reviews)