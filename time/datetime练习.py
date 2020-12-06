import datetime,time
a = datetime.datetime.now()
print(a)

b = datetime.datetime(2020,11,11,19,15,42)
print(b.year)
print(b.month)
print(b.day)
print(b.hour)
print(b.second)
print(b.minute)

print(datetime.datetime.fromtimestamp(time.time()))