#使用iter()返回一个可迭代的对象

a = list(range(5))
for i in iter(a):
    print(i)