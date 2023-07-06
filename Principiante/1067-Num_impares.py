x = int(input())

while x<=1 or x>1000:
    x = int(input())
    if x>=1 or x<=1000:
        break
for impar in range(x+1):
    if impar % 2 != 0:
        print(impar)