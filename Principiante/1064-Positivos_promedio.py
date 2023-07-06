u = float(input())
v = float(input())
w = float(input())
x = float(input())
y = float(input())
z = float(input())

val_pos=[]
suma=0

if u>=1:
    val_pos.append([u])
if v>=1:
    val_pos.append([v])
if w>=1:
    val_pos.append([w])
if x>=1:
    val_pos.append([x])
if y>=1:
    val_pos.append([y])
if z>=1:
    val_pos.append([z])

for line in val_pos:
    suma+=sum(line)
   
print(f'{len(val_pos)} valores positivos\n'
        f'{suma/len(val_pos):.1f}')
