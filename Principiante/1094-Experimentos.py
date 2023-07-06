N = int(input())
total = 0
c=0
r=0
s=0

for i in range(N):
    X,Y = map(str,input().split())
    num = int(X)
    if Y == 'C':
        total += num
        c += num

    elif Y == 'R':
        total += num
        r += num
    else:
        total += num
        s += num    

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c*100)/total:.2f} %')
print(f'Percentual de ratos: {(r*100)/total:.2f} %')
print(f'Percentual de sapos: {(s*100)/total:.2f} %')