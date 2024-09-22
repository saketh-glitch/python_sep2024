from database import Database
from inventory import Inventory
from generate_reports import Reports
from alerts import Alert_system
from authentication import Security
from transfer import Transfer_system
from prettytable import PrettyTable as pt
from reorder import l


def main():
    security = Security()
    inventory = Inventory()
    reports = Reports()
    alerts = Alert_system()
    transfers = Transfer_system()

    print("Welcome to the Inventory Management System \n")
    username = input("Enter your username: ")
    password = input("Enter your password: ") 
    user = security.authenticate(username, password) 

    while(True):
        if user :
            print("\n User authenticated successfully")
            break 
        else:
            print("Authentication failed... \n Try again ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = security.authenticate(username, password) 
        
    while True:
        print(f' \n Hello {username} , Welcome to your Inventory Management \n')
        print("     ACTIONS   \n")
        print("1. Add Material")
        print("2. View your inventory")
        print("3. Update your inventory")
        print("4. Generate Reports")
        print("5. Transfer Materials")
        print("6. Monitor Shipments")
        print("7. View shipments ")
        print("8. Delete material")
        print("9. Check if Reorder required")
        print("10. EXIT")

        choice = input(" \n Choose an action : ")
        
        if choice == '1':
            inventory.add_material()
        elif choice == '2':
            all=Database().fetch_all_materials()
            table=pt(['ID','Material','Qty in kg','Threshold','Price in Rs','Past_Sales'])
            for i in range(len(all)):
                table.add_row(all[i])  
            print(table)  
        elif choice == '3':
            inventory.update_inventory()   
        elif choice == '4':
            Reports().generate_inventory_report()
            Reports().generate_turnover_report()   
            Reports().forecast_demand() 
        elif choice == '5':
             transfers.transfer_material()
        elif choice=='6':
             shipment_id=input("Enter shipment id : ")
             trans=Database().monitor_shipment(shipment_id)
             table=pt(['ID','Mat_ID','Qty','Source','Dest','Time'])
             table.add_row(trans[0])
             print(table)
        elif choice == '7':  
            all_trans=Database().view_shipments()
            table=pt(['ID','Mat_ID','Qty','Source','Dest','Time'])
            for i in range(len(all_trans)):
                table.add_row(all_trans[i])
            print(table)     
        elif choice=='8':
            id=input("Enter the Material_id to delete : ")
            Database().remove_material(id)
        elif choice=='9':
            inventory.check_reorder()
        elif choice == '10':
            print("Exiting...") 
            break
        else:
            print(" ! Action is invalid, Please check...")
            continue

if __name__ == "__main__":
    main()