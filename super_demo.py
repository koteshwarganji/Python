#parent class/super class
class A:
    def __init__(self):
        print("constructor in A")
    def feature1(self):
        print("feature1 running")
    def feature2(self):
        print("feature2 running")
#child class/sub class
class B(A):
    def __init__(self):
        super(B, self).__init__()#calling parent class constructor
        print("constructor in B")
    def feature3(self):
        print("feature3 running")
    def feature4(self):
        print("feature4 running")

b1 = B()
b1.feature1()
b1.feature4()