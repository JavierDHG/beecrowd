n=int(input())

for i in range(n):
    a=int(input())
    count=0
    for x in range(1,a+1):
        total=a%x
        if total==0:
            count+=1
            total=0
    if count>2:
        print(f"{a} nao eh primo")
    else:
        print(f"{a} eh primo")