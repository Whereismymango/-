def max_len(*lists):
    return max(*lists)#max函数一般是比较多个数字的大小得到最大的那个数，但是也可以比较
                      #列表，是按照列表第一个元素比较的

a = max_len(list(range(1,10)),list(range(2,5)),[1,2,3])
print(f'最长的列表是{a}')


def max_len1(*lists):
    return max(*lists,key = lambda x:len(x))

a = max_len1(list(range(1,10)),list(range(2,5)),[1,2,3])
print(f'最长的列表是{a}')