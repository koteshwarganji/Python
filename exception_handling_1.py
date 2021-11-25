#Exception Handling: abnormal behaviour while running a program
#compile time errors : syntax errors
#run time errors : exceptions

try:
    print("try block")
    a = int(input("Enter a value : "))
    b = int(input("Enter b value : "))
    print(a/b)
except Exception as e:
    print("except block")
    print(e)
finally:
    print("finally block")