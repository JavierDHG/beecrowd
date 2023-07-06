t=int(input())

n=[]
x=0
for i in range(1000):
    n.append(x)
    x+=1
    if x==t:
        x=0
for a,b in enumerate(n):
    print(f"N[{a}] = {b}")
