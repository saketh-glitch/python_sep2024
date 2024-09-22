from database import Database
from reorder import Reorder_stock

class Inventory:
    def __init__(self):
        self.db = Database()

    def add_material(self):
        """Allow user to add a new material"""
        while(True):
            try:
             Item_id = int(input("Enter Item ID: "))
             Name = input("Enter Material Name: ")
             Stock = float(input("Enter initial stock: "))
             Reorder_threshold = float(input("Enter reorder threshold: "))
             Price_of_material = float(input("Enter Price of material : "))
             Historical_sales = float(input("Enter historical sales: "))
            except ValueError:
                print("Item id can be only integer, Name can be a string, Rest of all should be decimal values ")
                pass
            else:
                break
        self.db.add_material((Item_id, Name, Stock, Reorder_threshold, Price_of_material, Historical_sales))
        print(f'\n Material {Name} with ID {Item_id} added successfully to the Inventory !') 

    def update_inventory(self):
        """Allow user to update inventory"""  
        item_id = int(input("Enter Material ID to update : "))
        quantity = float(input("Enter new quantity : "))
        reorder_threshold=float(input("Enter the reorder threshold :"))  
        self.db.update_material_stock(item_id, quantity,reorder_threshold)
        print(f" \n Material with id {item_id} has been updated successfully")   
        print("-------------------------------------------------------------")

    def check_reorder(self):
        """Check if any item needs reordering"""
        all_materials = self.db.fetch_all_materials()

        for material in all_materials:
            Item_id, Name, Stock, Reorder_threshold, _, _ = material
            if Stock <= Reorder_threshold:
                print(f"Reordering material: {Name} (ID: {Item_id}) - Stock: {Stock}")
                self.update_inventory() 
            else:
                print("All are upto threshold stock ")

