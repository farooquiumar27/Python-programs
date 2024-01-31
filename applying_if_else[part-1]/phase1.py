a=input("Enter marks of Physics(0-100) : ")
try:
    physics=float(a)
    if physics.is_integer( )==False: exit( )
    else: physics=int(physics)
except:
    print(f"Invalid input {a}")
    exit( )
if physics<0 or physics>100:
    print(f"Invalid input {physics}")
    exit( )
a=input("Enter marks of Chemistry(0-100) : ")
try:
    chemistry=float(a)
    if chemistry.is_integer( )==False: exit( )
    else: chemistry=int(chemistry)
except:
    print(f"Invalid input {a}")
    exit( )
if chemistry<0 or chemistry>100:
    print(f"Invalid input {chemistry}")
    exit( )
a=input("Enter marks of Maths(0-100) : ")
try:
    maths=float(a)
    if maths.is_integer( )==False: exit( )
    else: maths=int(maths)
except:
    print(f"Invalid input {a}")
    exit( )
if maths<0 or maths>100:
    print(f"Invalid input {maths}")
    exit( )
a=input("Enter marks of English(0-100) : ")
try:
    english=float(a)
    if english.is_integer( )==False: exit( )
    else: english=int(english)
except:
    print(f"Invalid input {a}")
    exit( )
if english<0 or english>100:
    print(f"Invalid input {english}")
    exit( )
a=input("Enter marks of Hindi(0-100) : ")
try:
    hindi=float(a)
    if hindi.is_integer( )==False: exit( )
    else: hindi=int(hindi)
except:
    print(f"Invalid input {a}")
    exit( )
if hindi<0 or hindi>100:
    print(f"Invalid input {hindi}")
    exit( )
if physics>=33 and chemistry>=33 and maths>=33 and english>=33 and hindi>=33: print("Result: Pass")
elif physics<33 and chemistry>=33 and maths>=33 and english>=33 and hindi>=33: print("Result: Supp")
elif physics>=33 and chemistry<33 and maths>=33 and english>=33 and hindi>=33: print("Result: Supp")
elif physics>=33 and chemistry>=33 and maths<33 and english>=33 and hindi>=33: print("Result: Supp")
elif physics>=33 and chemistry>=33 and maths>=33 and english<33 and hindi>=33: print("Result: Supp")
elif physics>=33 and chemistry>=33 and maths>=33 and english>=33 and hindi<33: print("Result: Supp")
else: print("Result: Fail")