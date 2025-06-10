import sqlite3

# Connect to a database file (creates it if it doesn't exist)
conn = sqlite3.connect('dbexample2.db')
cursor = conn.cursor()

# Create a new table for sensor data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        Date DATE,
        SensorID TEXT,
        SensorType TEXT,
        Length INTEGER
    )
''')

# Insert the provided sensor data
events = [
    ("05/02/2023", "WS2", "Window", 38),
    ("05/02/2023", "MS1", "Motion", 2),
    ("06/02/2023", "DS3", "Door", 1),
    ("06/02/2023", "MS2", "Motion", 3),
    ("06/02/2023", "MS1", "Motion", 2),
    ("07/02/2023", "WS1", "Window", 24),
    ("07/02/2023", "DS1", "Door", 1)
]
cursor.executemany(
    'INSERT INTO events (Date, SensorID, SensorType, Length) VALUES (?, ?, ?, ?)',
    events
)
conn.commit()

# Example query: get all motion sensor events
cursor.execute('SELECT * FROM events')
events = cursor.fetchall()


# TODO Write a program that:
#  • asks the user to input a date
#  • totals the number of seconds sensors have been activated on the date input
#  • outputs the calculated total in an appropriate message including the date, for example:
#  Sensors were activated for 40 seconds on 05/02/2023





# Close the connection
conn.close()