a=10
b=20
c=a+b
print("Total of ",a,"and",b,"is",c)
print("Total of %d and %d is %d"%(a,b,c))
print("Total of {} and {} is {}".format(a,b,c))
print("Total of {} and {} is {}".format(b,c,a))
print("Total of {2} and {0} is {1}".format(b,c,a))
print("Total of {num1} and {num2} is {sum}".format(num1=a,num2=b,sum=c))
print(f"Total of {a} and {b} is {c}")
print(f"Total of {a} and {b} is {a+b}")