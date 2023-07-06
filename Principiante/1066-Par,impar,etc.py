w = int(input())
x = int(input())
y = int(input())
z = int(input())
zz = int(input())

valores=[]
valores_pares = []
valores_impares = []
valores_pos = []
valores_neg = []

valores.append(w)
valores.append(x)
valores.append(y)
valores.append(z)
valores.append(zz)

for valor in valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    if valor % 2 !=0:
        valores_impares.append(valor)
    if valor>0:
        valores_pos.append(valor)
    if valor<0:
        valores_neg.append(valor)

print(f'{len(valores_pares)} valor(es) par(es)')
print(f'{len(valores_impares)} valor(es) impar(es)')
print(f'{len(valores_pos)} valor(es) positivo(s)')
print(f'{len(valores_neg)} valor(es) negativo(s)')




'''
Manera mas efectiva

even=0
odd=0
positive=0
negative=0
for i in range(5):
    n = float(input())
    if(n % 2 == 0):
         even = even+1
    else:
        odd =odd+1
    if (n > 0):
        positive =positive+1
    elif (n < 0):
        negative =negative+1
print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{positive} valor(es) positivo(s)")
print(f"{negative} valor(es) negativo(s)")
'''