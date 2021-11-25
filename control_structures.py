#if else statements
x = int(input("Enter a number : "))
if x%2==0:
    print("even number")
else:
    print("odd number")

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

if a>b and a>c:
    print("a is biggest ",a)
elif b>c:
    print("b is biggest ",b)
else:
    print("c is biggest ",c)

