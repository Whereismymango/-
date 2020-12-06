#使用type()函数查看
class Student():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def run(self):
        pass

a = Student(1,2,3)
print(type(a))