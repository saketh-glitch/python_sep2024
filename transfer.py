from database import Database

class TransferSystem:
    def __init__(self):
        self.db = Database()

    def transfer_material(self):
        """Transfer material from one warehouse to another"""
        source_id = int(input("Enter source warehouse ID: "))
        dest_id = int(input("Enter destination warehouse ID: "))
        material_id = int(input("Enter material ID to transfer: "))
        quantity = int(input("Enter quantity to transfer: "))
        
        print(f"Transferring {quantity} units of material {material_id} from warehouse {source_id} to warehouse {dest_id}.")
        # Simulate update in stock for transfer
        self.db.update_material_stock(material_id, -quantity)