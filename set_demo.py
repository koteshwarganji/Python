#set is collection of unique elements
#set does not support indexing
#set never follows sequence

s = {10,11,12,13,14,11,12}
print(s)
s.update({13,14,15,16,17}) #update set with other set
print(s)
s.add(18)#add single element to set
print(s)
s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
print(s1.union(s2))#union
print(s1.intersection(s2))#intersection
print(s1.difference(s2))#minus
s1.discard(30)#removes elements
print(s1)