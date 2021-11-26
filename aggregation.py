#Aggregation : If class A owns class B.
#commonly known as "has-A" relationship.
#ex : Customer has-A Address
#Just like Customer "has-a" name, Customer "has-a" age, Customer "has-a" phone_no, now Customer also "has-a" Address

class Customer:
    def __init__(self,name,age,phone,address):
        self.name = name
        self.age = age
        self.phone = phone
        self.address  = address
    def view(self):
        print(self.name,self.age,self.phone)
        print(self.address.door_no,self.address.street,self.address.area,self.address.pincode)
    def update_details(self):
        pass
class Address:
    def __init__(self,door_no,street,area,pincode):
        self.door_no = door_no
        self.street = street
        self.area = area
        self.pincode = pincode
    def update_address(self):
        pass

add1 = Address(123,"excel street","excel area",508252)
cust = Customer("jack",24,1234,add1)
cust.view()
print(cust.address.door_no)