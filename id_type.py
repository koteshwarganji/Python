#id : returns the address of variable
#type : returns the type of variable

num = 5
print(id(num))
num2 = num
print(id(num2))
num2 = 10
print(id(num),id(num2))
num1 = 10
print(id(num1),id(num2))

print(type(10.12))
print(type(10))
print(type('koteshwar'))
print(type([10,20,30,40,50]))
print(type((10,20,30,40,50)))
print(type({1:'one',2:'two'}))
print(type({1,2,3,4}))
print(type(True))