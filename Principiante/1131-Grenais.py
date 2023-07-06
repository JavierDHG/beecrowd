registros=0
empate=0
W_Inter=0
W_Gremio=0

while True:
    Inter,Gremio=map(int,input().split())
    if Inter==Gremio:
        empate+=1
    elif Inter>Gremio:
        W_Inter+=1
    elif Inter<Gremio:
        W_Gremio+=1
    registros+=1
    X = int(input("Novo grenal (1-sim 2-nao)\n"))
    if X==1:
        pass
    else:
        break

print(f'{registros} grenais')
print(f'Inter:{W_Inter}')
print(f'Gremio:{W_Gremio}')
print(f'Empates:{empate}')
if W_Inter==W_Gremio:
    print("Não houve vencedor")
elif W_Inter>W_Gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")