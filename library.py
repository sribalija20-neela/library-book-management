books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    books.append({"title": title, "author": author, "year": year})
    print(f'✅ "{title}" added successfully!\n')

def view_books():
    if not books:
        print("📭 No books in the library.\n")
        return
    print("\n📚 All Books:")
    print("-" * 40)
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
    print("-" * 40 + "\n")

def search_book():
    keyword = input("Enter title or author to search: ").lower()
    results = [b for b in books if keyword in b['title'].lower() or keyword in b['author'].lower()]
    if results:
        print("\n🔍 Search Results:")
        for b in results:
            print(f"  - {b['title']} by {b['author']} ({b['year']})")
    else:
        print("❌ No matching books found.")
    print()

def delete_book():
    title = input("Enter the title of the book to delete: ").lower()
    for book in books:
        if book['title'].lower() == title:
            books.remove(book)
            print(f'🗑️ "{book["title"]}" deleted successfully!\n')
            return
    print("❌ Book not found.\n")

def menu():
    while True:
        print("=== Library Book Management System ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

menu()