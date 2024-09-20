from database import Database

class Inventory:
    def __init__(self):
        self.db = Database()

    def add_material(self):
        """Allow user to add a new material"""
        item_id = int(input("Enter Item ID: "))
        name = input("Enter Material Name: ")
        stock = int(input("Enter initial stock: "))
        reorder_threshold = int(input("Enter reorder threshold: "))
        cost_of_goods_sold = float(input("Enter cost of goods sold: "))
        historical_sales = float(input("Enter historical sales: "))

        self.db.add_material((item_id, name, stock, reorder_threshold, cost_of_goods_sold, historical_sales))

    def update_inventory(self):
        """Allow user to update inventory"""
        item_id = int(input("Enter Material ID to update: "))
        quantity = int(input("Enter quantity to add: "))
        self.db.update_material_stock(item_id, quantity)

    def check_reorder(self):
        """Check if any item needs reordering"""
        all_materials = self.db.fetch_all_materials()
        for material in all_materials:
            item_id, name, stock, reorder_threshold, _, _ = material
            if stock <= reorder_threshold:
                print(f"Reordering material: {name} (ID: {item_id}) - Stock: {stock}")
                self.update_inventory()