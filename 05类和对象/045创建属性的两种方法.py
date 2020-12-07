#第一种方法
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    
    def get_age_fun(self):
        print('这个p.AGE不是赋值的那个p.AGE')
        return self.__age
    
    def set_age_fun(self, value):        
        self.__age = value

    AGE = property(get_age_fun,set_age_fun,'35')
p = Person('balala',20)
p.AGE = 18
print(p.AGE)





#第二种方法
class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def get_age_fun(self):        
        return self.__age
    @get_age_fun.setter
    def set_age_fun(self, value):        
        self.__age = value

    
p = Person('balala',20)
p.set_age_fun = 18
print(p.get_age_fun)
#以上两种方法都比较难与解释，详细讲解见https://blog.csdn.net/weixin_45715405/article/details/106804366，或者第二种方法见https://www.ixigua.com/6804610049898447374/?is_new_connect=0&is_new_user=0