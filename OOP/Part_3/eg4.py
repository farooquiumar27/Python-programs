class Rectangle:
    def setLength(self,length):
        self.length=length
    def getLength(self):
        return self.length
    def setBreath(self,breath):
        self.breath=breath
    def getBreath(self):
        return self.breath
class Box(Rectangle):
    def setHeight(self,height):
        self.height=height
    def getHeight(self):
        return self.height
x=Box( )
x.setLength(10)
x.setBreath(2)
x.setHeight(5)
print("Lenght : ",x.getLength())
print("Breath : ",x.getBreath())
print("Height : ",x.getHeight())