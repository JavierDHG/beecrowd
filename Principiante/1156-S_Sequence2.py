x=2
resul=0
for i in range(3,40,2):
    resul+=(i/x)
    total=x*2
    x=total
    resul=resul
print(f'{(resul+1):.2f}')