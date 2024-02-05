class TMRange:
    def __init__(k,start,end,step=1):
        k.start=start
        k.end=end
        k.current=k.start
        k.step=step
    def __str__(k):
        return f"TMRange({k.start,k.end})"
    def __iter__(k):
        return k
    def __next__(k):
        if k.current>k.end: raise StopIteration
        data=k.current
        k.current=k.current+k.step
        return data
x=TMRange(1,5)
print(x)
for u in x:
    print(u)
j=TMRange(50,60,5)
for m in j:
    print(m)