class Classname:
    count = 81    
    def __init__(self,name):
        self.name = name
    def b(self):
        print('实例方法')
        print(Classname.count)
        Classname.count = 10000



    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):        
        print('类方法')
        print(Classname.count)

    

print(dir(Classname))