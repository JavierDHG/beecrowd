x=[]
k=[]
while x!=20:
    n=int(input())
    x.append(n)
    if len(x)==20:
        break
lista=reversed(x)

for s in lista:
    k.append(s)
for a,b in enumerate(k):
    print(f"N[{a}] = {b}")