#polymorphism : many forms
#one name many forms
#duck typing
#operator overloading,method overriding

#duck typing : same function behaves as a multiple behaviours
class Pycharm:
    def execute(self):
        print("compiling")
        print("running")
class MyIde:
    def execute(self):
        print("compiling")
        print("running")
        print("case checking")
        print("validation checking")
class Laptop:
    def code(self,obj):
        obj.execute()

ide1 = Pycharm()
ide2 = MyIde()
laptop1 = Laptop()
laptop1.code(ide1)
laptop1.code(ide2)
