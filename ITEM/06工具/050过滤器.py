#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。

f = filter(lambda x: x%2 == 1,list(range(10)))#注意要用双等号，单等号会报错
print(list(f))


#或者不用lambda方法，而是直接定义判断函数
def run(i):
    return i%2 == 1

a = list(range(10))
f = filter(run,a)
print(tuple(f))