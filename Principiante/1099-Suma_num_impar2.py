N = int(input())

for j in range(N):
    X,Y = map(int,input().split())
    if X > Y:
        star = Y
        end = X
        numeros = []

        for impar in range(star+1,end):
            if impar % 2 != 0:
                numeros.append(impar)
        print(sum(numeros))
    else:
        star = X
        end = Y
        numeros1 = []

        for impar in range(star+1,end):
            if impar % 2 != 0:
                numeros1.append(impar)
        print(sum(numeros1))