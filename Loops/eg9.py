steps =int(input("Enter number of steps : "))
star=1
space=steps-star
e=1
while e<=steps:
    f=1
    while f<=space:
         print(" ",end='')
         f+=1
    f=1
    while f<=star:
         print("*",end='')
         f+=1
    print()
    star+=2
    space-=1
    e+=1