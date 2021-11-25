a = 100
b = 200
print(a+b)
print(int.__add__(a,b))
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __sub__(self, other):
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        s3 = Student(m1,m2)
        return s3
    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s3 = Student(m1,m2)
        return s3
    def __str__(self):
        return str(self.m1)+' '+str(self.m2)

s1 = Student(100,100)
s2 = Student(90,80)
print(s1,s2)
print(s1+s2)
print(s1-s2)
print(s1*s2)


