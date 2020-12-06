class Big:
    def r(self):
        pass


class Small(Big):
    def run(self):
        pass

print(issubclass(Small,Big))
print(issubclass(Big,object))


#另外，如果calss是某个元组中某个元素的子类，也会返回True
print(issubclass(int,(int,str)))