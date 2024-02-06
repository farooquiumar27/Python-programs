class TMRange:
    def __init__(self,start,end="#",step=1):
        if isinstance(start,int)==False : raise TypeError("int required only")
        elif isinstance(step,int)==False : raise TypeError("int required only")
        elif end!="#" and isinstance(end,int,)==False : raise TypeError("int required only")
        elif step==0  : raise Error("Step cannot be zero")
        if end=="#" :
            self.start=1
            self.end=start
        else:
            self.start=start
            self.end=end
        self.step=step
        if start>end and step>0 : raise Error("Senseless expression")
    def __str__(self):
        return f"TMRange({self.start},{self.end})"
    def __iter__(self):
        iterator=TMRangeIterator(self)
        return iterator
class TMRangeIterator:
    def __init__(self,obj):
        self.start=obj.start
        self.end=obj.end
        self.step=obj.step
        self.current=self.start
        self.flag= 1 if self.step>0 else -1
    def __str__(self):
        return f"TMRangeIterator({self.start},{self.end})"
    def __next__(self):
        if (self.flag*self.current)>(self.flag*self.end) : raise StopIteration
        data=self.current
        self.current+=self.step
        return data
x=TMRange(5,1,-2)
for i in x:
    for j in x:
        for k in x:
            print(i,j,k)