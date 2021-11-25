from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1)
arr2 = arr1
print(arr1,arr2)
print(id(arr1),id(arr2))
#address is same becuase both
# are points to same location
arr2[3]=400
print(arr1,arr2)#arrays are mutable in python,both arrays have 400
print(id(arr1),id(arr2))#both have same address still

