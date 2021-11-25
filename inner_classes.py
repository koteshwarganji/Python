#inner classes : a class inside another class
class Customer:
    def __init__(self,cust_id,bill_amount,street,city):
        self.cust_id = cust_id
        self.bill_amount = bill_amount
        self.address = self.Address(street,city)
        #create a object of Address class
    def show_customer(self):
        print(self.cust_id,self.bill_amount)
    class Address:
        def __init__(self,street,city):
            self.street = street
            self.city =  city
        def show_address(self):
            print(self.street,self.city)

cust1 = Customer("c1001",1200,"excel-street","excel-city")
cust1.show_customer()
cust1.address.show_address()
