from numpy import *
arr1 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1)
print(arr1.ndim,arr1.shape,arr1.dtype)#2 (3,3) int32
print(arr1.size)#9
arr2 = arr1.flatten()#multi dimension to single dimension
print(arr2)

arr3 = arr2.reshape(3,3)#reshape to multi dimensional array
print(arr3)

brr1 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
brr2 = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
m1 = matrix(brr1)
m2 = matrix(brr2)
print(m1,m2)
print(m1+m2)
print(m1-m2)
print(m1*m2)
print(m1.diagonal())
print(m1.shape)#(3,3)
print(m1.ndim)#2
print(m1.dtype)#int32