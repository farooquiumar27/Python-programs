class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
class Box(Rectangle):
    def __init__(self,length,breath,height):
        super().__init__(length,breath)
        self.height=height
x=Box(10,2,5)
print("Lenght : ",x.length)
print("Breath : ",x.breath)
print("Height : ",x.height)
