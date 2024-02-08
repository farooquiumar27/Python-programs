import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(20);
a.append(30);
print(a.index(30))
print(a.index(300))