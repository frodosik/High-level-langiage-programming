from typing import Dict, Optional


class Library:
    def __init__(self) -> None:
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn, None)


if __name__ == "__main__":
    library = Library()
    library.add_book("978-83-01-12345-6", "Pan Tadeusz")
    library.add_book("978-83-01-54321-0", "Lalka")

    isbn_to_find = "978-83-01-12345-6"
    title = library.find_book(isbn_to_find)
    if title:
        print(f"Książka o ISBN {isbn_to_find}: {title}")
    else:
        print(f"Książka o ISBN {isbn_to_find} nie została znaleziona.")
