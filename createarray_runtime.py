from array import *
vals = array('i',[])#creating an empty array
size = int(input("Enter a size of an array : "))
for i in range(size):
    ele = int(input("Enter a element : "))
    vals.append(ele)#add single element
print(vals)

#simple search
key = int(input("enter element to search : "))
for ele in vals:
    if ele == key:
        print("element found at ",vals.index(ele))
        break
else:
    print("element not found")
