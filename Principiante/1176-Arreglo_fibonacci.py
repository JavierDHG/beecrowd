n=int(input())

c=0

while c<n:
    t=int(input())
    n1,n2=0,1
    for i in range(t):
        sum=n1+n2
        n1=n2
        n2=sum
    c+=1
    print(f'Fib({t}) = {n1}')