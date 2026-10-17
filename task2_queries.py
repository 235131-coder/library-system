import sqlite3

# Database connection & creation
conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'Data Science Basics', 'Tech', 1450, 10),
(2, 'Clean Code', 'Tech', 1200, 8),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'Python Crash Course', 'Tech', 950, 15),
(5, 'To Kill a Mockingbird', 'Fiction', 800, 3),
(6, 'Atomic Habits', 'Self-Help', 1100, 12),
(7, '1984', 'Fiction', 750, 4),
(8, 'The Great Gatsby', 'Fiction', 650, 6);
""")
conn.commit()

# Query (a): Price > 1000 sorted descending
print("--- Books above Rs.1000 (sorted) ---")
cur.execute("SELECT title, price FROM books WHERE price > 1000 ORDER BY price DESC;")
for row in cur.fetchall():
    print(row)

# Query (b): Rename title as book_title using AS
print("\n--- Renamed Column (book_title) ---")
cur.execute("SELECT title AS book_title, price FROM books LIMIT 3;")
for row in cur.fetchall():
    print(row)

# Query (c): Low-stock Fiction books (stock < 5)
print("\n--- Low-stock Fiction books ---")
cur.execute("SELECT title, genre, price, stock FROM books WHERE genre = 'Fiction' AND stock < 5;")
for row in cur.fetchall():
    print(row)

conn.close()