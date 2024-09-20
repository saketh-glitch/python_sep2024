from inventory import Inventory
from generate_reports import Reports
#from alerts import AlertSystem
from authentication import Security
from transfer import TransferSystem

def main():
    security = Security()
    inventory = Inventory()
    reports = Reports()
    #alerts = AlertSystem()
    transfers = TransferSystem()

    print("Welcome to the Inventory Management System")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user = security.authenticate(username, password)
    if not user:
        print("Authentication failed.")
        return



    while True:
        print("\n1. Add Material")
        print("2. Update Inventory")
        print("3. Check Reorder")
        print("4. Generate Reports")
        print("5. Monitor Shipments")
        print("6. Transfer Materials")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            inventory.add_material()
        elif choice == '2':
            inventory.update_inventory()
        elif choice == '3':
            inventory.check_reorder()
        elif choice == '4':
            reports.generate_turnover_report()
       # elif choice == '5':
            #alerts.monitor_shipments()
        elif choice == '6':
            transfers.transfer_material()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()