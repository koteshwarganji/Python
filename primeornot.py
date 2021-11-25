#check prime num or not
num = int(input("Enter a number to check : "))
i=1
count = 0
while i<=num:
    if num%i == 0:
        count=count+1
    i=i+1

if count == 2:
    print("prime number : ",num)
else:
    print("not a prime number : ",num)