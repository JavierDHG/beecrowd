x = float(input())

if x <= 2000:
    print("Isento")
elif x >=2000.01 and x<=3000:
    total=x-2000
    impuestos=total*0.08
    print(f"R$ {impuestos:.2f}")
elif x >=3000.01 and x<=4500:
    total=x-3000
    impuestos=(0.08*1000)+(0.18*total)
    print(f"R$ {impuestos:.2f}")
else:
    total=x-4500
    impuestos=(0.08*1000)+(0.18*1500)+(0.28*total)
    print(f"R$ {impuestos:.2f}")