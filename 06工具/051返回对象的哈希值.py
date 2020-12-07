#返回对象的哈希值，注意对象都是不可变对象，比如列表、集合、字典等可变对象是不能哈希的

print(hash('xiaoming'))
a = list(range(10))
print(hash(a))