import array
a=array.array('i');
a.append(10);
a.append(20);
a.append(30);
a.append(40);
a.append(20);
a.append(30);
a.remove(30)
for u in a : print(u)
a.remove(300)
for u in a : print(u)