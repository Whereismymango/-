a = list(range(11))
for i,j in enumerate(a):
    print(i,j)
print('\n')



a = list(range(11))
for i,j in enumerate(a,10):#第二个参数10指定从10开始索引
    print(i,j)
print('\n')


a = list(range(11))
b = enumerate(a)
print(next(b))#b为一个可枚举的对象，该对象的next()方法将依次返回一个元组
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))