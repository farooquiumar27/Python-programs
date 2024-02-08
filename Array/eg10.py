import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(20);
a.append(30);
a.insert(0,500);
for u in a : print(u)