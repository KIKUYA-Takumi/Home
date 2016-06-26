class Prism:
    def __init__(self,width,height,depth,unit='cm'):
        self.width = width
        self.height = height
        self.depth = depth
        self.unit = unit

    def content(self):
        return self.width * self.height * self.depth

    def unit_content(self):
        return str(self.content()) + self.unit

class Cube(Prism):
    def __init__(self,length):
        super().__init__(length,length,length)
        self.width = self.height = self.depth = length

class Prop(object):
    def __init__(self):
        self.__x = 0
    def getx(self):
        return self.__x
    def setx(self,x):
        self.__x = x
    x = property(getx,setx)


i = Prop()
print(i.x)

i.x = 19
print(i.x)

print(i._Prop__x)
