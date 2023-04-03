from lms.library_management_system import Book, Library, Member

# Instantiating three members_books
print("Instantiating three books:")
cryptonomicon = Book("Cryptonomicon", "Neil Stephenson")
neuromancer = Book("Neuromancer", "William Gibson")
merchant_princess = Book("The Merchant Princess, "
                         "The Family Trade", "Charles Stross")

# Instantiating two members
print("Instantiating two members:")
alice = Member(name="Alice")
bob = Member(name="Bob")

# Instantiating a library
print("Instantiating a library:")
library = Library("My Library")
print("Empty lib:\n", library)

# Adding members_books to the library
print("Adding members_books to the library:")
print(library.add_book(cryptonomicon, 2))
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

# One copy of the cryptonomicon has to be removed
library.remove_book(cryptonomicon, 1)
print(f"Library:\n{library}")
print(f"Bob wants to borrow the {cryptonomicon.title} by {cryptonomicon.author}:")
print(f" {library.borrow_book(cryptonomicon, bob)}")
print(f"Alice wants to read {cryptonomicon.title} by {cryptonomicon.author}:")
print(f" {library.borrow_book(cryptonomicon, alice)}")
