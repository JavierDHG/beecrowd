N = int(input())

for i in range(1,N+1):
    b=i*i
    c=i*i*i
    print("{} {} {}".format(i,b,c))
    a=b+1
    d=c+1
    print("{} {} {}".format(i,a,d))