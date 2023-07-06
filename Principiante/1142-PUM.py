n=int(input())
a,b,c=1,2,3
for i in range(1,n+1):
    print("{} {} {} PUM".format(a,b,c))
    a+=4
    b+=4
    c+=4

"""
numero = 1

for _ in range(6):  # Imprime 6 filas
    for _ in range(3):  # Imprime 3 números por fila
        print(numero, end=' ')
        numero += 1
    print("PUM")
    numero += 1
"""