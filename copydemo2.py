from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
#view function used to created a shallow copy
#new array is created at different location
#but if value changed in one array also reflects in another array
#it is called shallow copy
print(id(arr1),id(arr2))#addresses are different
arr2[3]=400
print(id(arr1),id(arr2))#addresses are different
print(arr1,arr2)#both will have value 400