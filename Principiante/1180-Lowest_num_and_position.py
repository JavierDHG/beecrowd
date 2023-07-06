n=int(input())
a=list(map(int,input().split()))
l=a[0]

for i in a:
    if i<l:
        small=min(a)
        pos_small=a.index(small)
        print(f"Menor valor: {small}\nPosicao: {pos_small}")
        break