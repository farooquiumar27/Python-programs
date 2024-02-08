import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(20);
a.append(30);
print(a.count(30))
print(a.count(300))
print(a.count(3.3))
