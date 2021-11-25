#global : variable declared outside the functions
#variable scope is entire program
#local variable : variable declared within functions
#variable scope is within the function itself

a = 10
b = 100
def something():
    a = 20
    print("local var : ",a)#20
    c = globals()['a']+a
    print("c value : ",c)#10+20
    global b
    b = b + 10
    print("b value : ",b)#110
something()
print("global var : ",a)#10
print("b value : ",b)#110