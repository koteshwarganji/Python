x = int(input("enter a range :"))
for i in range(x):
    if(i%2==0):
        continue#skips current iteration and continues with next iteration
    if(i==5):
        break#exit from loop
    if(i%2==1):
        pass#empty statement
    print(i,end=" ")


