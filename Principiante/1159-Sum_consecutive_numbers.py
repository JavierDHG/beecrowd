a=1

while a==1:
    x=int(input())
    if x==0:
        break
    else:
        if x%2==0:
            j=x
            c=0
            for i in range(1,6):
                c+=j
                j+=2
            print(c)
        else:
            j=x+1
            c=0
            for i in range(1,6):
                c+=j
                j+=2
            print(c)