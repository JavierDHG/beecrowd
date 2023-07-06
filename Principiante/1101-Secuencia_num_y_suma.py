while True:
    M,N = map(int,input().split())
    if M<=0 or N<=0:
        break
    elif M>N:
        star=N
        end=M
        sum=0
        nums=[]
        for i in range(star,end+1):
            sum+=i
            nums.append(i)
        print(f" ".join(map(str,nums)),f"Sum={sum}")
    else:
        star=M
        end=N
        sum=0
        nums=[]
        for i in range(star,end+1):
            sum+=i
            nums.append(i)
        print(f" ".join(map(str,nums)),f"Sum={sum}")