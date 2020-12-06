#十进制分别转化为二进制、八进制、十六进制

#内置函数bin、oct、hex实现转换
a = list(range(100,140,7))
print([bin(i) for i in a])#bin实现转换，会带进制前缀'0b',返回字符串
print([oct(i) for i in a])#oct实现转换，会带进制前缀'0o',返回字符串
print([hex(i) for i in a],'\n')#hex实现转换，会带进制前缀'0x',返回字符串

#format实现转换
print([format(i,'b') for i in a])#format()返回字符串，要返回数字按下式进行
#print([int(format(i,'b')) for i in a])
print([format(i,'o') for i in a])
print([format(i,'x') for i in a],'\n')




#二进制、八进制、十六进制转化为十进制
b = [bin(i) for i in a]
#b = [format(i,'b') for i in a] b也可以写为这样，后面的print语句输出结果一样
c = [oct(i) for i in a]
d = [hex(i) for i in a]
print([int(i,2) for i in b])#i可以是带前缀'0b'，也可以不带
print([int(i,8) for i in c])
print([int(i,16) for i in d])