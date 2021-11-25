#generator : emits the sequence of elements

def topTen():
    n = 0
    while n<=10:
        yield n
        n=n+1

values = topTen()
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(list(values))