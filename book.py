class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        if self.is_issued:
            raise Exception("Book is already issued.")
        self.is_issued = True

    def return_book(self):
        if not self.is_issued:
            raise Exception("Book is not currently issued.")
        self.is_issued = False

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"]
        )
        book.is_issued = data.get("is_issued", False)
        return book