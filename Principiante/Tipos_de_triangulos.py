A,B,C = map(float,input().split())
numeros = [A,B,C]
numeros.sort(reverse=True)
A = numeros[0]
B = numeros[1]
C = numeros[2]
if A >= B+C :
    print("NAO FORMA TRIANGULO")
elif A**2 == ((B**2)+(C**2)):
    print("TRIANGULO RETANGULO")
elif A**2 > ((B**2)+(C**2)):
    print("TRIANGULO OBTUSANGULO")
if A**2 < ((B**2)+(C**2)):
    print("TRIANGULO ACUTANGULO")
if A==B==C:
    print("TRIANGULO EQUILATERO")
if A==B!=C or A!=B==C or A==C!=B or A!=C==B :
    print("TRIANGULO ISOSCELES")