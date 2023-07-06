x=[]
while x!=100:
    n=float(input())
    x.append(n)
    if len(x)==100:
        break
for a,b in enumerate(x):
    if b<=10:  
        print(f"A[{a}] = {b}")