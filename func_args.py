def person(name,age,salary):
    print(name,age,salary)

person("ganji koteshwar",24,300000)#positional args
person(age=25,salary=400000,name="g koti")#keyword args

#default args
def new_person(name="alien",age=18,salary=25000):
    person(name,age,salary)

new_person(None,None,None)#None None None
new_person("koti g")#koti g 18 25000


