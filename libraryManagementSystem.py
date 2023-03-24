"""This is the library management system.

A Project to show Classes and the SOLID principles in a 2 hour workshop."""
from typing import Optional, Dict, List


class Book:
    """This is the Book class.

    It kees track of a book in the library."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __repr__(self) -> str:
        return f'{self.title} by {self.author}'


class Library:

    def __init__(self, name: str, inventory: Optional[Dict[Book, int]] = None):
        self.name = name
        self.inventory = inventory or {}

    def __repr__(self) -> str:
        return f'{self.name}, {len(self.inventory)} different books:\n' \
               f' {self.inventory}\n'

    def add_book(self, book: Book, quantity: int = 1) -> str:
        if book not in self.inventory:
            self.inventory[book] = 0
        self.inventory[book] += quantity
        return f'{quantity} copies of "{book.title}" by {book.author}.\n'

    def remove_book(self, book: Book, quantity: int = 1) -> str:
        if book in self.inventory:
            self.inventory[book] -= quantity
            if self.inventory[book] <= 0:
                del self.inventory[book]
                return f"{quantity} copies of {book} removed from inventory\n"
        else:
            raise ValueError(f'{book} not in inventory')

    def borrow_book(self, book: Book, member: 'Member') -> str:
        if book in self.inventory:
            if self.inventory[book] > 0:
                self.inventory[book] -= 1
                member.books.append(book)
                return f"{book.title} is now borrowed by {member.name}\n"
            else:
                raise ValueError(f'{book} not available')
        else:
            raise ValueError(f'{book} not in inventory')

    def return_book(self, book: Book, member: 'Member') -> str:
        if book in self.inventory:
            if book in member.books:
                self.inventory[book] += 1
                member.books.remove(book)
                return f"{book} returned by {member}"
            else:
                raise ValueError(f'{member} does not have {book}')
        else:
            raise ValueError(f'{book} not in inventory')


class Member:
    """This is the Member class.

    It keeps track of a member of the library and the borrowed books."""

    def __init__(self,
                 name: str,
                 books: Optional[List[Book]] = None):
        self.name = name
        self.books = books or []

    def __repr__(self) -> str:
        return f'{self.name}, has: {len(self.books)} books'
