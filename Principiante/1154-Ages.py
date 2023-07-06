a=[]
while True:
    resuldato=0
    n=int(input())
    if n>0:
        a.append(n)
        total=sum(a)
    else:
        break

resuldato=total/len(a)  
print(f'{resuldato:.2f}')