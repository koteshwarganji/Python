#datatypes : None,list,tuple,set,dict,set,string,range,dict
#None : indicates absence of a value
a = None
print(a,type(None))
name = 'ganji koteshwar'
print(name,type(name))
id = 1075580
print(id,type(id))
experience = 2.3
print(experience,type(experience))
isMarried = False
print(isMarried,type(isMarried))
c = 9+6j
print(c,type(c))
n1 = 100
n2 = 200
comp = complex(n1,n2)
print(comp,type(comp))
print(comp.real,comp.imag)
#type conersions
print(int(2.3))
print(float(2))
print(int(True),int(False))
# print('1'+1)#error
print(int('1')+1)#2
print(str(1)+'1')#11
print(list(range(10)))#0->9
print(list(range(0,10)))#0->9
print(list(range(0,10,2)))#0,2,,4,6,8