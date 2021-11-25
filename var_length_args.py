def sum(a,*b):
    s=a
    print(a,b)
    for i in b:
        s = s+i
    print("sum : ",s)

sum(10)#10
sum(10,20,30,40)#100
sum(10,20)#30