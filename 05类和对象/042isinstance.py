#判断是否为类的实例
class Student():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def run(self):
        pass

a = Student(1,2,3)
xiaoming = 1
print(isinstance(a,Student))
print(isinstance(xiaoming,Student))