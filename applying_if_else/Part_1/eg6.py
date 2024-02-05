x=int(input("Enter a number : "))
try:
    if x==0: exit( )
except SystemExit as e:
    print("Some problem")
print(x)