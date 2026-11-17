# Lab 14(a) - Initial Data Setup

books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

# Extract unique categories
library_categories = set()

for book in books:
    library_categories.add(book[3])

# Student wishlist
student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}

print("Books:", books)
print("Library Categories:", library_categories)
print("Student Wishlist:", student_wishlist)