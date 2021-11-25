#method overriding : creation of method in child class same as that of parent class

class A:
    def show(self):
        print("show in A")
class B(A):
    def show(self):
        super(B, self).show()#calling parent class show method
        print("show in B")
b1 = B()
b1.show()