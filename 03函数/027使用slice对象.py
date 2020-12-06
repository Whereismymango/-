a = list(range(5,0,-1))
print(a)
b = a[1:10:2]
print(b,'\n')

from random import randint
c = [randint(1,100) for i in range(100)]
#不一定列表推导式中的结果就必须含有i，比如上面这一行randint(1,100)就没有
d = c[1:10:2]
print(d,'\n')


#上面两个运行均使用切片[1:10:2]，可以一次性把切片封装为一个对象，多次调用就是
s = slice(1,10,2)#这里每个数之间是逗号而不是冒号
print(a[s])
print(d)
print(c[s])

