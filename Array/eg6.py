import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(50);
x=0
ep=len(a)-1
while x<=ep:
    print(a[x])
    x+=1