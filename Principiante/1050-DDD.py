a = int(input())

b=[61,71,11,21,32,19,27,31]

if a == 61:
    city = 'Brasilia'
if a == 71:
    city = 'Salvador'
if a == 11:
    city = 'Sao Paulo'
if a == 21:
    city = 'Rio de Janeiro'
if a == 32:
    city = 'Juiz de Fora'
if a == 19:
    city = 'Campinas'
if a == 27:
    city = 'Vitoria'
if a == 31:
    city = 'Belo Horizonte'
elif a in b:
    print(city)
else:
    print('DDD nao cadastrado')


'''
Solucion mas efectiva
a=int(input())
if a==61:
    print("Brasilia")
elif a==71:
    print("Salvador")
elif a==11:
    print("Sao Paulo")
elif a==21:
    print("Rio de Janeiro")
elif a==32:
    print("Juiz de Fora")
elif a==19:
    print("Campinas")
elif a==27:
    print("Vitoria")
elif a==31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
'''