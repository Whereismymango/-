class Classname:
    count = 81
    # 普通方法
    def __init__(self,name):
        self.name = name
    def b(self):
        print('实例方法')
        print(Classname.count)#实例方法内部可以访问类属性
        Classname.count = 10000#实例方法内部可以修改类属性



    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        #self.name = '实例属性能被类方法修改吗'    #类方法内部不能修改实例属性
        #print(self.name) #类方法内部也不能调用实例属性
        print('类方法')
        print(Classname.count)

    

c = Classname('Jack')#实例对象可以调用静态方法、类方法以及实例方法
print(c.count)#实例对象可以调用实例属性
c.b()
c.fun()
c.a()

Classname.fun()#只能类调用静态方法
Classname.a()#类可以调用类方法

