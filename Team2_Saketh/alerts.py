import smtplib as smtp
class Alert_system():
    def monitor_shipments(self,source,destination,id,quantity):
        self.source=source
        self.destination=destination
        self.id=id
        self.quantity=quantity
        connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        email_address = 'svmsaikrishna2002@gmail.com' #Add your email here
        email_password = 'esgc csnq sisq qlai' #password given by google
        connection.login(email_address, email_password)
        connection.sendmail(from_addr=email_address, to_addrs='svmsk1911@gmail.com', msg=f' Shipment Alert : \n {quantity} units of material with id {id} has been successfully transferred from {source} to {destination}')
        connection.close()  
        print(' Shipment alert has been sent successfully  ! ')    

        
    def reorder_stock(id):
        connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
        email_address = 'svmsaikrishna2002@gmail.com' #Add your email here
        email_password = 'esgc csnq sisq qlai' #password given by google 
        connection.login(email_address, email_password)
        connection.sendmail(from_addr=email_address, to_addrs='svmsk1911@gmail.com', msg=f'Material with id {id} has been out of stock. Hence it is reordered as per requirement')

