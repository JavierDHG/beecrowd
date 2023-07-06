x=[]
while x!=10:
    n=int(input())
    x.append(n)
    if len(x)==10:
        break
for a,b in enumerate(x):
    if b<=0:
        x[a]=1
for a,b in enumerate(x):    
    print(f"X[{a}] = {b}")