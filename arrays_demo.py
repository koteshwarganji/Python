#arrays : list of elements,similar elements,do not have fixed size
from array import *
val = array('i',[10,20,30,40,50])
print(val,type(val))
print(val.typecode)
val.reverse()
print(val)
print(len(val))
print(val[0],val[len(val)-1])
for a in val:
    print(a,end=" ")
print()
print("############################")
vowels = array('u',['a','e','i','o','u'])
print(vowels,type(vowels))
for ch in vowels:
    print(ch,end=" ")