print("pattern-1")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

print("pattern-2")
for i in range(5):
    for j in range(5):
        if j<=i:
            print("*",end="")
    print()
print("pattern-3")
for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end="")
        else:
            print(" ",end="")
    print()
