#astract classes :
#We can implement abstract classes using abc module
#We can not create a object for abstract class
#abstract class should have atleast one abstract method
#abstract classes can have non-abstract methods
#the child classes of abstract classes implement abstract methods
#of abstract classes
#we can create objects for child classes

from abc import *
class Product(ABC):
    @abstractmethod
    def pay_bill(self):pass
    def info(self):
        print("product class information")
class Mobile(Product):
    def pay_bill(self):
        print("pay bill method in Mobile")
    def process(self):
        print("Mobile class process methods")
mob1 = Mobile()
mob1.pay_bill()
mob1.process()
mob1.info()