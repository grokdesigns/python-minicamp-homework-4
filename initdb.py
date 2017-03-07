import sqlite3

connection = sqlite3.connect('database.db')
print('We\'ve opened the database successfully!')

connection.execute('CREATE TABLE friends (name TEXT, age INTEGER)')
print('Table created successfully!')

connection.close()
