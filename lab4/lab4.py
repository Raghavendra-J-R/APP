"""
4. Implement Library management where students can borrow as well as donate books.
Books table:
•	id INTEGER PRIMARY KEY
•	name TEXT
•	total_count INTEGER
a)	Insert values to the table
34,king,5
123,Harry Potter,3
b)	Update the table based on user inputs: 
based on book id
I)	BORROW 

"""

import sqlite3

# Connect to the database (create it if it doesn't exist)
conn = sqlite3.connect("library.db")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create Books table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Books (
                id INTEGER PRIMARY KEY,
                name TEXT,
                total_count INTEGER)"""
)

# Insert initial values into the table
books_data = [(34, "king", 5), (123, "Harry Potter", 3)]

print(type(books_data))

cursor.executemany(
    """INSERT INTO Books (id, name, total_count)
                    VALUES (?, ?, ?)""",
    books_data,
)

# Commit the changes to the database
# conn.commit()


# Function to borrow a book
def borrow_book(book_id):
    cursor.execute("""SELECT total_count FROM Books WHERE id = ?""", (book_id,))
    result = cursor.fetchone()
    if result:
        total_count = result[0]
        if total_count > 0:
            cursor.execute(
                """UPDATE Books SET total_count = ? WHERE id = ?""",
                (total_count - 1, book_id),
            )
            conn.commit()
            print("Book borrowed successfully.")
        else:
            print("Book not available for borrowing.")
    else:
        print("Book not found.")


# Function to return a book
def return_book(book_id):
    cursor.execute("""SELECT total_count FROM Books WHERE id = ?""", (book_id,))
    result = cursor.fetchone()
    if result:
        total_count = result[0]
        cursor.execute(
            """UPDATE Books SET total_count = ? WHERE id = ?""",
            (total_count + 1, book_id),
        )
        conn.commit()
        print("Book returned successfully.")
    else:
        print("Book not found.")


# User interaction
while True:
    print("\nLibrary Management System")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter the book ID to borrow: "))
        borrow_book(book_id)
    elif choice == "2":
        book_id = int(input("Enter the book ID to return: "))
        return_book(book_id)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Close the cursor and connection
cursor.close()
conn.close()
