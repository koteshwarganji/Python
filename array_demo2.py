import array as arr
vals = arr.array('i',[10,11,12,13,14,15])
print(vals)
#creating a new array using old array
newVals = arr.array(vals.typecode,[a for a in vals])
print(newVals)
#addresses are different
print(id(vals),id(newVals))

for a in newVals:
    print(a,end=",")
