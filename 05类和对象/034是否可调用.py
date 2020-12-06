#callable()检查对象是否可以被调用

print(callable(str))
print(callable(int),'\n')

class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def repr(self):
        print('fndisnfdis')
        return 'id = ',self.id,'name = ',self.name


xiaoming = Student('001','xiaoming')
print(callable(xiaoming),'\n')
#调用xiaoming后返回false，说明小明不能被调用，因为xiaoming()什么也不打印或者返回
#如果想调用xiaoming，需要重写Student类的__call__方法
class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def repr(self):
        return 'id = ',self.id,'name = ',self.name
    def __call__(self):
        print('I can be called')
        print(f'my name is {self.name}')
xiaobin = Student('002','xiaobin')
print(callable(xiaobin))
xiaobin()#此时就会被调用打印
# I can be called
# my name is xiaobin