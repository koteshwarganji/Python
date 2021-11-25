#inheritance : creation of child classes using parent classes
#single level : one parent , one child
#parent class/super class
class A:
    def feature1(self):
        print("feature1 running")
    def feature2(self):
        print("feature2 running")
#child class/sub class
class B(A):
    def feature3(self):
        print("feature3 running")
    def feature4(self):
        print("feature4 running")

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()