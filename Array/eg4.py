import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(50);
x=0
while x<=4:
    print(a[x])
    x+=1