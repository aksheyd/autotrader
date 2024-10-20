import sqlite3
import os

# Connect to the database (or create it if it doesn't exist)
database_path = '/Users/aksheydeokule/Documents/autotrader/database/stock_prices.db'
conn = sqlite3.connect(database_path)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create a table for storing stock information
cursor.execute('''
CREATE TABLE IF NOT EXISTS stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()