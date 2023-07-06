c=0
x = int(input())
c+=1
sum=x
z = int(input())
while z<=x:
    z = int(input())
    if z>x:
        for i in range(x+1,z):
            sum+=i
            c+=1
            if sum>z:
                break
print(c)