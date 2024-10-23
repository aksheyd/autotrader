import sqlite3
import os

class database:
    def __init__(self, type):
        if type != 'stocks' and type != 'nancy':
            raise ValueError('Invalid database type')
        
        self.type = type
        self.database_path = os.path.join(f'../database/{self.type}.db')

    def create_stocks_table(self):
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        self.conn.close()
    
    def create_nancy_table(self):
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS nancy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        self.conn.close()
    
    def create(self):
        if self.type == 'stocks':
            self.create_stocks_table()
        elif self.type == 'nancy':
            self.create_nancy_table()
    
    def insert(self, data):
        self.conn = sqlite3.connect(self.database_path)
        self.cursor = self.conn.cursor()

        for item in data:
            self.cursor.execute('''
            INSERT INTO stocks (name, price, date, time)
            VALUES (?, ?, ?, ?)
            ''', (item['name'], item['price'], item['date'], item['time'])
            )

        self.conn.commit()
        self.conn.close()