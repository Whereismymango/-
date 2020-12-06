def sumx(i):
    
    def func():
        nonlocal i#nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
        i += 1
        print(sum(list(range(i))))
    return func()
sumx(3)



'''以下3个函数，第一个正常，而2跟3会报错，因为第一个内层函数无赋值无修改，
   可以调用外层函数局部变量；而2跟3内层函数进行了修改操作，这就决定了num
   和lst只能是内层函数的局部变量，而在修改前也没有声明，所以报错'''
   
def func1(lst=[]):
    def inner_func():
        lst.append(10)
        print(lst)
        return lst
    return inner_func()

def func2(num=10):
    def inner_func():
        num += 1
        return num
    return inner_func()


def func3(lst=[]):
    def inner_func():
        lst += [10]
        return lst
    return inner_func()

func1(lst=[2])
func2(num=10)
func3(lst=[])