while True:
    a=1
    X = int(input())
    if X==0:
        break
    else:
        for _ in range(1):
            for _ in range(1,X):
                print(_, end=' ')
                a+=1             
            print(X)
            a=1

'''
Mejor solucion
while True:
    x = int(input())
    if x == 0:
        break
    else:
        for b in range(1, x):
            print(b, end=' ')
        print(x)
'''