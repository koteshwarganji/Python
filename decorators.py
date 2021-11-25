def div(a,b):
    print("division ",a/b)

def smart_div(func):
    print("address of func ",id(func))
    def inner(a,b):
        print("address of inner ",id(inner))
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

print("address of div ",id(div))
div = smart_div(div)
print("address of div ",id(div))
div(20,30)