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

    def read(self) -> str:
        return f'{self.title} by {self.author} is being read.'


class Library:
    """This is the Library class.

    It keeps track of the books in the library."""

    def __init__(self, name: str, inventory: Optional[Dict[Book, int]] = None):
        self.name = name
        self.inventory = inventory or {}

    def __repr__(self) -> str:
        return f'{self.name}, {len(self.inventory)} different books:\n' \
               f' {self.inventory}'

    def add_book(self, book: Book, quantity: int = 1) -> str:
        """Add a book to the library.

        If the book is already in the library, increase the quantity.
        If the book is not in the library, add it to the library.

        Returns a string with the book title and author.

        Parameters
        ----------
        book : Book
            The book to add to the library.
        quantity : int, optional
            The number of copies to add to the library, by default 1.

        Returns
        -------
        str
            A string with the book title and author.

        Examples
        --------
        >>> library = Library("My Library")
        >>> b1 = Book("1984", "George Orwell")
        >>> library.add_book(b1, quantity=2)
        '2 copies of "1984" by George Orwell added to inventory.'
        >>> library.add_book(b1)
        '1 copies of "1984" by George Orwell added to inventory.'
        >>> library.inventory
        {1984 by George Orwell: 3}
        """

        if book not in self.inventory:
            self.inventory[book] = 0
        self.inventory[book] += quantity
        return f'{quantity} copies of "{book.title}" by {book.author} added ' \
               f'to inventory.'

    def remove_book(self, book: Book, quantity: int = 1) -> str:
        """
        Remove a book from the library.

        Parameters
        ----------
        book : Book
            The book to be removed from the library.
        quantity : int, optional
            The number of copies of the book to remove (default is 1).

        Returns
        -------
        str
            A message indicating the number of copies of the book that were
            removed from the library.

        Raises
        ------
        ValueError
            If the book is not in the library.

        Examples
        --------
        >>> library = Library("My Library")
        >>> b1 = Book("1984", "George Orwell")
        >>> library.add_book(b1, quantity=2)
        '2 copies of "1984" by George Orwell added to inventory.'
        >>> library.remove_book(b1)
        '1 copies of "1984" by George Orwell removed from inventory.'
        >>> library.remove_book(b1, quantity=2)
        '2 copies of "1984" by George Orwell removed from inventory.'
        """

        if book in self.inventory:
            self.inventory[book] -= quantity
            if self.inventory[book] <= 0:
                del self.inventory[book]
            return f'{quantity} copies of "{book.title}" by {book.author} removed ' \
                   f'from ' \
                   f'inventory.'
        raise ValueError(f'{book} not in inventory')

    def borrow_book(self, book: Book, member: 'Member') -> str:
        """
        Borrow a book from the library.

        Parameters
        ----------
        book : Book
            The book to be borrowed from the library.
        member : Member
            The member who is borrowing the book.

        Returns
        -------
        str
            A message indicating that the book has been borrowed.

        Raises
        ------
        ValueError
            If the book is not available or is not in the library.

        Examples
        --------
        >>> library = Library("My Library")
        >>> b1 = Book("1984", "George Orwell")
        >>> alice = Member("Alice")
        >>> library.add_book(b1, 2)
        '2 copies of "1984" by George Orwell added to inventory.'
        >>> library.borrow_book(b1, alice)
        '1984 is now borrowed by Alice.'
        """
        if book in self.inventory:
            if self.inventory[book] > 0:
                self.inventory[book] -= 1
                member.books.append(book)
                return f"{book.title} is now borrowed by {member.name}."
            raise ValueError(f'{book} not available')
        else:
            raise ValueError(f'{book} not in inventory')

    def return_book(self, book: Book, member: 'Member') -> str:
        """
        Return a book to the library.

        Parameters
        ----------
        book : Book
            The book to be returned to the library.
        member : Member
            The member who is returning the book.

        Returns
        -------
        str
            A message indicating that the book has been returned.

        Raises
        ------
        ValueError
            If the book is not available or is not in the library, or if the member
            does not have the book.

        Examples
        --------
        >>> library = Library("My Library")
        >>> b1 = Book("1984", "George Orwell")
        >>> alice = Member("Alice")
        >>> library.add_book(b1, 2)
        '2 copies of "1984" by George Orwell added to inventory.'
        >>> library.borrow_book(b1, alice)
        '1984 is now borrowed by Alice.'
        >>> library.return_book(b1, alice)
        '1984 returned by Alice'
        """
        if book in self.inventory:
            if book in member.books:
                self.inventory[book] += 1
                member.books.remove(book)
                return f"{book.title} returned by {member.name}"
            raise ValueError(f'{member} does not have {book}')
        else:
            raise ValueError(f'{book} not in inventory')


class Member:
    """This is the Member class.

    It keeps track of a member of the library and the borrowed books."""

    def __init__(self, name: str, books: Optional[List[Book]] = None):
        self.name = name
        self.books = books or []

    def __repr__(self) -> str:
        return f'{self.name}, has: {len(self.books)} books'
