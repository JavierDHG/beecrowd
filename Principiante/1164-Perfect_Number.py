n=int(input())

for i in range(n):
    a=int(input())
    total=0
    for x in range(a):
        total=total+x
        if total==a or total>=a:
            break
    if total==a:
        print(f"{a} eh perfeito")
    else:
        print(f"{a} nao eh perfeito")