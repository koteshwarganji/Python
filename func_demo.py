#functions definition
def greet():
    print("Hello World")
#function call
greet()

def add(a,b):
    print("addition is : ",a+b)
add(10,20)

def sub(a,b):
    return a-b
print("substraction is ",sub(20,10))
def add_sub(a,b):
    return a+b,a-b
res1,res2 = add_sub(30,10)
print(res1,res2)
