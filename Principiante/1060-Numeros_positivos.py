u = float(input())
v = float(input())
w = float(input())
x = float(input())
y = float(input())
z = float(input())

val_pos=[]

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
    print(f'{len(val_pos)} valores positivos')