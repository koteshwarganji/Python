def person(name,**kwargs):
    print(name,kwargs)#dictionary
    for k,v in kwargs.items():
        print(k,':',v)

person("gkoteshwar")
person("gkoti",age=21,sal=500000)
