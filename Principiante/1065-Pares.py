w = int(input())
x = int(input())
y = int(input())
z = int(input())
zz = int(input())

valores_pares = []

if w % 2 == 0:
    valores_pares.append(w)
if x % 2 == 0:
    valores_pares.append(x)
if y % 2 == 0:
    valores_pares.append(y)
if z % 2 == 0:
    valores_pares.append(z)
if zz % 2 == 0:
    valores_pares.append(zz)

print(f'{len(valores_pares)} valores pares')
