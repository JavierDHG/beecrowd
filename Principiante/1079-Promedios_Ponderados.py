N = float(input())

for i in range(int(N)):
    x,y,z = list(map(float,input().split()))
    result=(x*0.20+y*0.30+z*0.50)
    print(f'{result:.1f}')