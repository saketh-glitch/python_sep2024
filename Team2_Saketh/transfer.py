from database import Database  
from alerts import Alert_system
from datetime import datetime

class Transfer_system:
    def __init__(self):
        self.db = Database()

    def transfer_material(self):
        """Transfer material from one warehouse to another"""
        transaction_time=datetime.today()
        shipment_id=input("Enter an id for shipment : ")
        source_id = input("Enter source warehouse ID: ")
        dest_id = input("Enter destination warehouse ID: ")
        while(True):
           try:
            material_id = int(input("Enter material ID to transfer: "))
            quantity = int(input("Enter quantity to be transferred: "))
           except ValueError:
            print('material_id should be integer, quantity should be integer. ')
            print('Please check and enter')
            pass
           else:
            break
        re_list= Database().fetch_attribute(material_id) 
        reorder=re_list[0]
        print(f"Transferring {quantity} units of material {material_id} from warehouse {source_id} to warehouse {dest_id}.\n")
        # Simulate update in stock for transfer
        Database().add_transaction((shipment_id,material_id,quantity,source_id,dest_id,transaction_time))
        Database().transfer_update(material_id, quantity,reorder)     
        Alert_system().monitor_shipments(source_id,dest_id,material_id,quantity)   