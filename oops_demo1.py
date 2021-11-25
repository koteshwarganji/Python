#class : class is blue print/design from which we can create multiple objects
#object : object is a real world entity which exists unique
#method : behaviour of objects , functions in classes
#attribute : property of objects , variables in classes
#__init__ : constructors in classes , invoked during object creation
#self : indicates the current object
#objects are stored in heap memory,size of variable depends upon the no of variables

class Person:
    def __init__(self,name,age,salary):
        # print(self)
        self.name = name
        self.age = age
        self.salary = salary
    def set_salary(self,new_salary):
        self.salary = new_salary
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary

person1 = Person("ganji koteshwar",24,7000000)
print(person1.get_name(),person1.get_age(),person1.get_salary())
person2 = Person("g koti",25,8000000)
print(person2.get_name(),person2.get_age(),person2.get_salary())


