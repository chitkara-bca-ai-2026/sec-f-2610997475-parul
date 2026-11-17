# Lab 14(b) - Library Book Collection

while True:

    print("\n===== LIBRARY BOOK & CATEGORY MANAGER =====")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # View Books
    if choice == "1":

        print("\n--- Current Library Catalog ---")

        for i, book in enumerate(books, start=1):
            title, author, year, category = book

            print(f"{i}. {title} by {author} ({year})")
            print("Genre:", category)

        print("Total Books:", len(books))

    # Add New Book
    elif choice == "2":

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        if title and author and year and category:

            new_book = (title, author, year, category)

            books.append(new_book)
            library_categories.add(category)

            print("[SUCCESS] Book added successfully.")
            print("[INFO] Category set updated.")

        else:
            print("All fields are required.")

    # View Categories
    elif choice == "3":

        print("\n--- Unique Library Categories ---")

        for category in sorted(library_categories):
            print("-", category)

        print("Total Unique Genres:", len(library_categories))

    # Add to Wishlist
    elif choice == "4":

        category = input("Enter requested category: ")

        if category:
            student_wishlist.add(category)
            print("[SUCCESS] Category added to wishlist.")
        else:
            print("Category cannot be empty.")

    # Category Gap Analysis
    elif choice == "5":

        print("\n===== CATEGORY GAP ANALYSIS =====")

        print("Library Holdings:", library_categories)
        print("Student Wishlist:", student_wishlist)

        # Intersection
        available = library_categories.intersection(student_wishlist)

        # Difference
        missing = student_wishlist.difference(library_categories)

        # Union
        combined = library_categories.union(student_wishlist)

        print("\n1. Already in Stock (Intersection):")
        print(sorted(available))

        print("\n2. Purchase Order Needed (Difference):")
        print(sorted(missing))

        print("\n3. Full Combined Genre Coverage (Union):")
        print(sorted(combined))

    # Exit
    elif choice == "6":

        print("Thank you for using the Library Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Enter a number between 1 and 6.")