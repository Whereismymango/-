class Xiaoming():
    def __init__(self,namme,age):
        self.name = namme
        self.age = age

    def pr(self):
        pass

xiaoming = Xiaoming('xiaoming',18)    
print(hasattr(xiaoming,'name'))
print(hasattr(xiaoming,'age'))
print(hasattr(xiaoming,'salary'))