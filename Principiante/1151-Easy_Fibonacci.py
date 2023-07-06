N=int(input())

c=0
n1,n2=0,1
while c<N-1:
    print(n1, end=' ')
    sum=n1+n2
    n1=n2
    n2=sum
    c+=1
print(n1)