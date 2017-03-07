import sqlite3

connection = sqlite3.connect('database.db')
print('We\'ve opened the database successfully!')

connection.execute('CREATE TABLE movies (title TEXT, year INTEGER)')
print('Table created successfully!')

connection.close()
