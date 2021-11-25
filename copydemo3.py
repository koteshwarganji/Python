from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
#deep copy : new array will be created new location
#if we change the value of one array it wont reflected in another array
#is called a deep copy
print(id(arr1),id(arr2))#addresses are different
arr2[3]=400
print(arr1,arr2)#only arr2 will have 400
