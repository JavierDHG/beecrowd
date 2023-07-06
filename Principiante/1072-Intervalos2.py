X = int(input())

inside = 0
out = 0

i = 0
while i<X:
    N = int(input())
    if (10<=N<=20):
        inside+=1
        i+=1
    else:
        out+=1
        i+=1
print(f'{inside} in')
print(f'{out} out')