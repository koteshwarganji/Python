#object / instance variables : belongs to object,each object has separate copy f
#instance variables
#static variables :belongs to class,only one copy of static variables for all objects
#static varibales are accessed by using classname

#intstance methods : used to access instance variables
#class methods : class variables are used in class methods,we can't use instance variables.
#static methods : if you want to do nothing with instance and class variables.
class Person:
    company = 'software company'
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
    @classmethod
    def get_company(cls):
        return cls.company
    @staticmethod
    def info():
        print("this is a static methods")

person1 = Person("ganji koteshwar",24,7000000)
print(person1.get_name(),person1.get_age(),person1.get_salary())
person2 = Person("g koti",25,8000000)
print(person2.get_name(),person2.get_age(),person2.get_salary())
print(Person.company)
print(Person.get_company())
