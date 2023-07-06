alumnos=[]
N,K = map(int,input().split())
while N<1 or N>100 or K<1 or K>100 or K>N:
    N,K = map(int,input().split())
    if K<=N:
        if N>=1 and N<=100 and K>=1 and K<=100:
            break
while len(alumnos) <N:
    nombres = input()
    name = nombres.lower()
    if name.isalpha():
        if len(name) > 20 or len(name)==0:
            name = input()
        else:
            alumnos.append(name)
    else:
        name = input()
    if len(alumnos) == N:
        break
alumnos.sort()
print(alumnos[K-1])