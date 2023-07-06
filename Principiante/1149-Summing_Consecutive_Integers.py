sum=0
n=0
lista=list(map(int,input().split()))
a=lista[0]
lista.pop(0)
for x in lista:
    if x>0:
        n=x
    for i in range(0,n):
        suma=a+i
        sum+=suma
print(sum)