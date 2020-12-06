a = [1,4,2,3,1]
print(sorted(a))
print(sorted(a,reverse=True))

a.sort(reverse=True)
print(a)

from operator import itemgetter
a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':
     'xiaohong','age':20,'gender':'female'}]
print(sorted(a,key=itemgetter('age')))
print(sorted(a,key=lambda x:x['age']))