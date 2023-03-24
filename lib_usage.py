from library_management_system import Book, Library, Member

# Instantiating three members_books
cryptonomicon = Book("Cryptonomicon", "Neil Stephenson")
neuromancer = Book("Neuromancer", "William Gibson")
merchant_princess = Book("The Merchant Princess, "
                         "The Family Trade", "Charles Stross")

# Instantiating two members
alice = Member("Alice")
bob = Member("Bob")

# Instantiating a library
library = Library("My Library")
print("Empty lib: ", library)

# Adding members_books to the library
print(library.add_book(cryptonomicon, 1))
print(library)

library.add_book(neuromancer, 1)
print(library)

# Alice Books
print(f"Alice's books: '{alice.books}'\n")

# Borrowing a book
print(f"Using the borrow method: {library.borrow_book(neuromancer, alice)}")
print(library)

# Alice has the book now
print(f"Alice's books: '{alice.books}'")

# Returning a book
print("Alice returns a book: ", library.return_book(neuromancer, alice))
print(library)

library.remove_book(cryptonomicon, 1)
print(f"Alice wants to read a book by Neil Stephenson:")
print(f" {library.borrow_book(cryptonomicon, alice)}")
