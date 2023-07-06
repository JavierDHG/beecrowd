x=[]
n=int(input())
x.append(n)
for i in range(n,n*100,2):
    total=(n*2)
    n=total
    x.append(total)
    if len(x)==10:
        break
for a,b in enumerate(x):
    print(f"N[{a}] = {b}")