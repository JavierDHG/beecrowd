N = int(input())
nums = []


for i in range(0,N):
    X = int(input())
    nums.append(X)
for z in nums:
    if z == 0:
        print("NULL")
    elif z % 2 == 0:
        if z<0:
            print("EVEN NEGATIVE")
        else:
            print("EVEN POSITIVE")
    elif z % 2 != 0:
        if z<0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")


'''
Solucion Mejor

n=int(input())
for i in range(n):
    a=int(input())
    if(a<0):
        if(a%2==0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif(a>0):
        if(a % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif(a==0):
        print("NULL")
'''