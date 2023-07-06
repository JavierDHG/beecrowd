total=0
for i in range(2,101):
    total+=(1/i)
    sum=total
    total=sum
print(f'{(total+1):.2f}')