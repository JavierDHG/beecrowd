def num1():
    N1 = float(input())
    while True:
        if N1<0 or N1>10:
            print("nota invalida")
            N1 = float(input())
        else:
            break
    return N1

def num2():
    N2 = float(input())
    while True:
        if N2<0 or N2>10:
            print("nota invalida")
            N2 = float(input())
        else:
            break
    return N2

def result(numero1,numero2):
    if numero1>numero2:
        print(f"media = {((numero1+numero2)/2):.2f}")   
    else:
        print(f"media = {((numero2+numero1)/2):.2f}")
    return

def again():
    valor1=num1()
    valor2=num2()
    result(valor1,valor2)
    X = int(input("novo calculo (1-sim 2-nao)\n"))
    while True:
        if X>2 or X<0:
            X = int(input("novo calculo (1-sim 2-nao)\n"))
        elif X==1:
            valor1=num1()
            valor2=num2()
            result(valor1,valor2)
            X = int(input("novo calculo (1-sim 2-nao)\n"))
        else:
            break
again()