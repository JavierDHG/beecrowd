N1 = float(input())
while True:
    if N1<0 or N1>10:
        print("nota invalida")
        N1 = float(input())
    else:
        break
N2 = float(input())
while True:
    if N2<0 or N2>10:
        print("nota invalida")
        N2 = float(input())
    else:
        break

if N1>N2:
    print(f"media = {((N1+N2)/2):.2f}")
    
else:
    print(f"media = {((N2+N1)/2):.2f}")