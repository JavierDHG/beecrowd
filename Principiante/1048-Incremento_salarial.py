a=float(input())

if a>=0 and a<=400:
    print(f'Novo salario: {(a*0.15)+a:.2f}\nReajuste ganho: {a*0.15:.2f}\nEm percentual: 15 %')
if a>=400.01 and a<=800.00:
    print(f'Novo salario: {(a*0.12)+a:.2f}\nReajuste ganho: {a*0.12:.2f}\nEm percentual: 12 %')
if a>=800.01 and a<=1200.00:
    print(f'Novo salario: {(a*0.10)+a:.2f}\nReajuste ganho: {a*0.10:.2f}\nEm percentual: 10 %')
if a>=1200.01 and a<=2000.00:
    print(f'Novo salario: {(a*0.07)+a:.2f}\nReajuste ganho: {a*0.07:.2f}\nEm percentual: 7 %')
if a>=2000.01:
    print(f'Novo salario: {(a*0.04)+a:.2f}\nReajuste ganho: {a*0.04:.2f}\nEm percentual: 4 %')


'''
Solucion mas efectiva
a = float(input())
if(a>=0 and a<=400):
	b= a*0.15
	c=a+b
	d=15
elif(a>=400.01 and a<=800.00):
	b=a*0.12
	c=a+b
	d=12
elif(a>=800.01 and a<=1200.00):
    b=a*0.1
    c=a+b
    d=10
elif(a>=1200.01 and a<=2000.00):
	b=a*0.07
	c=a+b
	d=7
elif(a>2000):
	b=a*0.04
	c=a+b
	d=4
print(f"Novo salario: {c:.2f}")
print(f"Reajuste ganho: {b:.2f}")
print(f"Em percentual: {d} %")
'''