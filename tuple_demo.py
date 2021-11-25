#tuple in python are immutable
tup = (10,20,40,30,50)
print(tup)
#tup[1]=200#error because tuples are immutable
print(tup[0],tup[len(tup)-1])
tup2 = tup
print(id(tup),id(tup2))#points to same object
print(min(tup),max(tup),sum(tup))

