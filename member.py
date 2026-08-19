class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []

    def issue_book(self, book_id):
        self.issued_books.append(book_id)

    def return_book(self, book_id):
        if book_id not in self.issued_books:
            raise Exception("This book is not issued to this member.")
        self.issued_books.remove(book_id)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "issued_books": self.issued_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(
            data["member_id"],
            data["name"]
        )
        member.issued_books = data.get("issued_books", [])
        return member