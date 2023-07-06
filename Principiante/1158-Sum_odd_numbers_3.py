n=int(input())

for i in range(n):
    x,y=list(map(int,input().split()))
    if x%2==1:
        c=0
        for a in range(1,y+1):
            c=c+x
            x=x+2
        print(c)
    else:
        x+=1
        c=0
        for a in range(1,y+1):
            c+=x
            x+=2
        print(c)