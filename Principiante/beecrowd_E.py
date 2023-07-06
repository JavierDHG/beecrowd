A,E,N = map(int,input().split())
while A<=1 or A>100000 and E<=0 or E>100000 and N<=0 or N>100000:
    print("NO")
    break
while A<=100000 or E<=100000 or N<=100000:
    total = A+E+N
    f=0
    v=0
    if A>(E+N):
        print("YES")
        for i in range(1,total+1):
            if i<=(E+N):
                f+=1
            else:
                v+=1
            if v>f:
                print(v+f)
    break