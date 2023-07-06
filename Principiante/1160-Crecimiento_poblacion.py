t=int(input())

for i in range(t):
    pa,pb,g1,g2=input().split()
    pa=int(pa)
    pb=int(pb)
    g1=float(g1)
    g2=float(g2)
    years=0
    while pa<=pb:
        result1=int((pa*(g1/100)))
        result2=int((pb*(g2/100)))
        pa+=result1
        pb+=result2
        years+=1
        if years>100:
            break
    if years>100:
        print("Mais de 1 seculo.") 
    else:
        print(f"{years} anos.")