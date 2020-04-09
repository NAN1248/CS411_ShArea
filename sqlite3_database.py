import sqlite3

connection = sqlite3.connect('sql_database.db')

cursor = connection.cursor()

print(cursor.fetchall());
