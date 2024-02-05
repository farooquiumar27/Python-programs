class TMRange:
    def __init__(k,start,end):
        k.start=start
        k.end=end
        k.current=k.start
    def __str__(k):
        return f"TMRange({k.start,k.end})"
    def __iter__(k):
        return k
    def __next__(k):
        if k.current>k.end: raise StopIteration
        data=k.current
        k.current+=1
        return data
x=TMRange(1,5)
print(x)
for u in x:
    print("Outer",u)
    for j in x:
        print("Inner",j)