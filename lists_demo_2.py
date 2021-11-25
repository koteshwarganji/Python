nums = [10,20,40,50,30]#lists
print(nums)
nums.append(40)#append element at the end
print(nums)
nums.insert(3,100)#insert element at 3rd index
print(nums)
nums.remove(40)#remove element 40
print(nums)
nums.pop(2)#remove element at 2nd index
print(nums)
nums.pop()#remove last element
print(nums)
nums.extend([60,70,80])#add multiple elements
print(nums)
del nums[4:]#delete elements
print(nums)
print(min(nums))#print min element
print(max(nums))#print max element
print(sum(nums))#print sum of list
nums[3]=60#lists are mutable
print(nums)