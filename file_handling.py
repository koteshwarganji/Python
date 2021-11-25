#file handling : we have text files and binary files
f = open('text_file','r')
print(f)
# print(f.read())#read entire file content
# print(f.readline())#read one line at a time
# print(f.readline())
# print(f.readline())
# print(f.readlines())#read lines into a list

f2 = open('text_file_2','w')
for data in f:
    print(data)
    f2.write(data)#write data into a file

