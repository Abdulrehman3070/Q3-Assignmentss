import json

# File to store library data
LIBRARY_FILE = "library.txt"

def load_library():
    """Load library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read})
    print("Book added successfully!\n")
    save_library(library)


def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found!\n")
    save_library(library)

def search_books(library):
    """Search for books by title or author."""
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    keyword = input("Enter search keyword: ").lower()
    
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found!")
    print()

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty!\n")
        return
    print("Your Library:")
    for book in library:
        print(f"🔹 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    print()

def display_statistics(library):
    """Display total books and percentage read."""
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percent_read = (read_count / total * 100) if total > 0 else 0
    print(f"Total books: {total}\nPercentage read: {percent_read:.2f}%\n")

def main():
    """Main function to run the program."""
    library = load_library()
    
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
