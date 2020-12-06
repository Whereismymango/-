#类属性
class Coordinate():
    x = 11
    y = -6
    z = 1
point1 = Coordinate()
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)
delattr(Coordinate, 'z')
print('--删除 z 属性后--')
print('x = ', point1.x)
print('y = ', point1.y)
# 触发错误
#print('属性删除后 z = ',point1.z)


#实例属性
class Classname():    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
i = Classname(1,2,3)
print(i.a,i.b,i.c)
delattr(i,'c')#注意实例对象删的是实例的属性，不要把i错写为Classname,这里与上面删除类的属性区分开
print(i.a,i.b)
#print(i.a,i.b,i.c)由于删除了i的c属性，会报错
j = Classname(1,2,3)#上面delattr只是删除了实例对象i的属性，新建一个j对象，他仍然具有abc三个属性值，不会报错
print(j.a,j.b,j.c)
