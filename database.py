import sqlite3
from threading import Lock

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('inventory.db', check_same_thread=False)
        self.lock = Lock()
        self.create_tables()

    def create_tables(self):
        """Create necessary tables for inventory management"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS materials (
                              id INTEGER PRIMARY KEY,
                              name TEXT,
                              stock INTEGER,
                              reorder_threshold INTEGER,
                              cost_of_goods_sold REAL,
                              historical_sales REAL)''')
            self.conn.commit()

    def add_material(self, material):
        """Insert new material into database"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO materials (id, name, stock, reorder_threshold, cost_of_goods_sold, historical_sales)
                              VALUES (?, ?, ?, ?, ?, ?)''', material)
            self.conn.commit()

    def update_material_stock(self, item_id, quantity):
        """Update stock of an existing material"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''UPDATE materials SET stock = stock + ? WHERE id = ?''', (quantity, item_id))
            self.conn.commit()

    def fetch_material(self, item_id):
        """Fetch a material from the database"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT * FROM materials WHERE id = ?''', (item_id,))
            return cursor.fetchone()

    def fetch_all_materials(self):
        """Fetch all materials from the database"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT * FROM materials''')
            return cursor.fetchall()
