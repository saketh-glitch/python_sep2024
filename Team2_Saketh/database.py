import sqlite3
from threading import Lock
from reorder import Reorder_stock 

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('inventory_db', check_same_thread= False)
        self.lock = Lock()   
        self.create_tables()  

    def create_tables(self):
        """Create necessary tables for inventory management"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Materials (
                              Item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                              Name varchar(40) not null, 
                              Stock FLOAT(5,2) not null,
                              Reorder_threshold FLOAT(5,2),
                              Price_of_material REAL,
                              Historical_sales REAL)''') 
            self.conn.commit()

        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS transfer_log (
                              ID INTEGER PRIMARY KEY AUTOINCREMENT,
                              product_id INTEGER,
                              quantity INTEGER,
                              source_warehouse TEXT,
                              destination_warehouse TEXT,
                              transfer_date TEXT,
                              FOREIGN KEY(product_id) REFERENCES products(id) )''')
            self.conn.commit()
            

    def add_material(self, material):
        """Insert new material into database"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO Materials (Item_id, Name, Stock, Reorder_threshold, Price_of_material, Historical_sales)
                              VALUES (?, ?, ?, ?, ?, ?)''', material)
            self.conn.commit()

    def update_material_stock(self, item_id, quantity,reorder_threshold): 
        """Update stock of an existing material"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''UPDATE materials SET stock = ? , Reorder_threshold= ? WHERE Item_id = ?''', (quantity,reorder_threshold, item_id))
            self.conn.commit()   
            Reorder_stock().reorder(item_id,quantity,reorder_threshold) 
    
    def transfer_update(self,item_id,quantity,reorder_threshold):
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute(''' update materials set stock= stock- ?, Reorder_threshold= ? where Item_id=? ''',(quantity,reorder_threshold,item_id))
            self.conn.commit()
            Reorder_stock().reorder(item_id,quantity,reorder_threshold) 

    def fetch_material(self, Item_id):
        """Fetch a material from the database"""
        with self.lock:
            cursor = self.conn.cursor()  
            cursor.execute('''SELECT * FROM materials WHERE Item_id = ?''', (Item_id)) 
            return cursor.fetchone()

    def fetch_all_materials(self):
        """Fetch all materials from the database"""
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''SELECT * FROM materials''') 
            data=cursor.fetchall()   
            return data
    
    def remove_material(self,Item_id):
        '''Remove a material from the database'''
        with self.lock:
            cursor= self.conn.cursor()
            cursor.execute('''delete from Materials where Item_id = ? ''',(Item_id)) 
            self.conn.commit()  
            print(f"Material with id {Item_id} has been deleted successfully ")
    
    def fetch_attribute(self,Item_id):
        '''Fetch an attribute from database'''
        with self.lock:
            cursor= self.conn.cursor()
            cursor.execute(''' select Reorder_threshold from Materials where Item_id = ? ''', (Item_id,))  
            re = cursor.fetchone()
            return re 
        
    def add_transaction(self,transaction):
        '''Add to Transfer Log '''
        with self.lock:
            cursor= self.conn.cursor()
            cursor.execute('''INSERT into transfer_log (ID,product_id,quantity,source_warehouse,destination_warehouse,transfer_date) 
                           VALUES(?,?,?,?,?,?) ''',transaction) 
            self.conn.commit()

    def view_shipments(self):
        ''' View and monitor your shipments'''
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''select * from transfer_log ''')  
            data=cursor.fetchall()
            return data 
        
    def monitor_shipment(self,shipment_id):
        ''' View and monitor a particular shipment'''
        with self.lock:
            cursor = self.conn.cursor()
            cursor.execute('''select * from transfer_log where ID = ?''',(shipment_id,))
            data=cursor.fetchall()
            return data 





