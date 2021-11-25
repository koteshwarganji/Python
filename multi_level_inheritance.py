#multi level inheritance : parent -->child --->child
class A:
    def feature1(self):
        print("feature1 running")
    def feature2(self):
        print("feature2 running")
class B(A):
    def feature3(self):
        print("feature3 running")
    def feature4(self):
        print("feature4 running")
class C(B):
    def feature5(self):
        print("feature5 running")
    def feature6(self):
        print("feature6 running")

c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()
