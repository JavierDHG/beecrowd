par=[]
impar=[]

for i in range(15):
    n=int(input())
    if n%2==0:
        par.append(n)
        if len(par)==5:
            for a,b in enumerate(par):
                print(f"par[{a}] = {b}")    
            par.clear()
    if n%2==1:
        impar.append(n)
        if len(impar)==5:
            for a,b in enumerate(impar):
                print(f"impar[{a}] = {b}")    
            impar.clear()
for a,b in enumerate(impar):
    print(f"impar[{a}] = {b}")   

for a,b in enumerate(par):
    print(f"par[{a}] = {b}") 