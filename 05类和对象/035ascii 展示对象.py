class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        print('fndisnfdis')
        return 'id = '+self.id+'name = '+self.name


xiaoming = Student('001','xiaoming')
xiaoming.__repr__()
ascii(xiaoming.__repr__())