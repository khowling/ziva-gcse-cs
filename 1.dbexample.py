import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('dbexample1.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        StudentName TEXT PRIMARY KEY,
        Detail TEXT,
        Points INTEGER,
        LetterSent BOOLEAN
    )
''')

# Insert a row of data
students = [
    ("Kirstie", "Homework forgotten", -2, False),
    ("Byron", "Good effort in class", 1, True),
    ("Grahame", "100% in a test", 2, False),
    ("Marian", "Bullying", -3, True)
]
cursor.executemany(
    'INSERT OR REPLACE INTO students (StudentName, Detail, Points, LetterSent) VALUES (?, ?, ?, ?)',
    students
)
# Commit the changes
conn.commit()

# Query the database
cursor.execute('SELECT * FROM students where StudentName = "Kirstie"')

# studentdata contains the first row of the query result
studentdata = cursor.fetchall()[0]

# TODO: Write an algorithm that will identify whether the data in the studentdata array
#  shows that a letter has been sent home or not for the student. The algorithm should 
# then output either “sent” (if a letter has been sent) or “not sent” (if a letter has
#  not been sent)






# Close the connection
conn.close()