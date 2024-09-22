from alerts import Alert_system
l={}
class Reorder_stock:
    def reorder(self,item_id,quantity,reorder_threshold):

        while(True):
            if quantity< reorder_threshold:
                reorder_permission=input(f'Material with id {item_id} is out of threshold stock, do you want to reorder ? (yes/no)\n')
                if reorder_permission=="yes":
                    print(f'\n Material with id{item_id} has been ordered sucessfully...') 
                    print("--------------------------------------------------------------")
                    l['item_id']=item_id
                    l['quantity_reordered']=quantity 
                    Alert_system.reorder_stock(item_id)
                    print(f' Order confirmation has been sent to your registered Email-ID\n')
                    break
                else:
                    break   
            else:
                break
        pass