from numpy import *
arr = array([1,2,3,4,5])
print(arr)#print arrays
#add 5 to each element
arr = arr+5
print(arr)

arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])
#adding 2 arrays
print(arr1,arr2)
arr3 = arr1 + arr2
print(arr3)
#min value,max value,sum of elements in array
print(min(arr3),max(arr3),sum(arr3))
print(sqrt(arr3))#sqrt of each ele
print(log(arr3))#log of each ele
print(unique(arr3))#unique value of each element
print(concatenate([arr1,arr2]))#concatenate 2 arrays

