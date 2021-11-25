#different ways of creating arrays in numpy
#6 ways
#array(),linespace(),logspace(),arange(),zeros(),ones()

from numpy import *
#using array()
arr1 = array([10,20,30,40,50],int)
arr2 = array([10.0,11.1,12.2,13.3,14.4,15.5],float)
print(arr1,arr2)

#using linespace()
arr3 = linspace(1,10,10)#start end noofparts
print(arr3)
arr4 = linspace(1,10)#50 parts default
print(arr4)

#using logspace()
arr5 = logspace(1,10,10)#start end parts
print(arr5)
arr6 = logspace(1,10)#start end 50 parts default
print(arr6)

#using arange
arr7 = arange(1,10)#start end
print(arr7)
arr8 = arange(1,10,2)#start end step
print(arr8)

#using zeros
arr9 = zeros(5,int)
print(arr9)

#using ones
arr10 = ones(5,int)
print(arr10)

