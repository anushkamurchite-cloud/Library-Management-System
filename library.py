from book import Book
from member import Member
from file_handler import FileHandler


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

        self.load_data()

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise Exception("Book ID already exists.")

        self.books[book_id] = Book(book_id, title, author)
        self.save_data()
        print("Book added successfully.")

    def add_member(self, member_id, name):
        if member_id in self.members:
            raise Exception("Member ID already exists.")

        self.members[member_id] = Member(member_id, name)
        self.save_data()
        print("Member added successfully.")

    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            raise Exception("Book not found.")

        if member_id not in self.members:
            raise Exception("Member not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        book.issue_book()
        member.issue_book(book_id)

        self.save_data()
        print("Book issued successfully.")

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            raise Exception("Book not found.")

        if member_id not in self.members:
            raise Exception("Member not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        book.return_book()
        member.return_book(book_id)

        self.save_data()
        print("Book returned successfully.")

    def search_book(self, keyword):
        found = False

        for book in self.books.values():
            if (keyword.lower() in book.title.lower()
                    or keyword.lower() in book.author.lower()
                    or keyword == book.book_id):

                status = "Issued" if book.is_issued else "Available"

                print(
                    f"ID: {book.book_id} | "
                    f"Title: {book.title} | "
                    f"Author: {book.author} | "
                    f"Status: {status}"
                )

                found = True

        if not found:
            print("No book found.")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            status = "Issued" if book.is_issued else "Available"

            print(
                f"ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Author: {book.author} | "
                f"Status: {status}"
            )

    def view_members(self):
        if not self.members:
            print("No members available.")
            return

        for member in self.members.values():
            print(
                f"ID: {member.member_id} | "
                f"Name: {member.name} | "
                f"Issued Books: {member.issued_books}"
            )

    def save_data(self):
        books_data = [
            book.to_dict()
            for book in self.books.values()
        ]

        members_data = [
            member.to_dict()
            for member in self.members.values()
        ]

        FileHandler.save_data("books.json", books_data)
        FileHandler.save_data("members.json", members_data)

    def load_data(self):
        books_data = FileHandler.load_data("books.json")
        members_data = FileHandler.load_data("members.json")

        for data in books_data:
            book = Book.from_dict(data)
            self.books[book.book_id] = book

        for data in members_data:
            member = Member.from_dict(data)
            self.members[member.member_id] = member