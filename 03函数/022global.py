i = 1
def h():
    print(i)
    return i

def g():
    global i
    i += 1
    print(i)
    return i
h()#不报错是因为函数内无修改无赋值，是可以调用全局变量的
g()#如果没有global语句就会报错，因为函数内有修改，这就决定了i为局部而非全局变量，可是
   #i在函数内又没有定义，所以会报错
print(i)