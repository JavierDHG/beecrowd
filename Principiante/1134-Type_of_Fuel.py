alcohol=0
gasoline=0
diesel=0


while True:
    fuel=int(input())
    if fuel==1:
        alcohol+=1
    elif fuel==2:
        gasoline+=1
    elif fuel==3:
        diesel+=1
    elif fuel==4:     
        break
print("MUITO OBRIGADO")
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasoline}')
print(f'Diesel: {diesel}')