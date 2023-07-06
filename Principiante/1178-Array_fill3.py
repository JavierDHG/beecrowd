x=float(input())

n=[]
n.append(x)
a=0
for i in range(99):
    a=x/2
    x=a
    n.append(a)

for a,b in enumerate(n):
    print(f"N[{a}] = {b:.4f}")