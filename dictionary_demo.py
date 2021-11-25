d = dict() #create a empty dictionary
print(d)
d["name"] = "ganji koteshwar"
d["phone"] = 6300297881
d["email"] = "koteshwarganji@gmail.com"
print(d)
print(d.get("name"))#get value using key
print(d.keys())#list of keys
print(d.values())#list of values
print(d.items())#list of key,value pairs
print(d.setdefault("id",1075580))#insert id if id is not in dictionary
print(d)
value1= [1,2,3,4,5]
value2= ['one','two','three','four','five']
data = dict(zip(value1,value2))
print(data)
data = list(zip(value1,value2))
print(data)
data = tuple(zip(value1,value2))
print(data)
data = set(zip(value1,value2))
print(data)