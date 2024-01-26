import sqlite3

con = sqlite3.connect("employee.db")
print("Database opened successfully")

con.execute("create table user (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")

print("Table created successful")

con.close()
