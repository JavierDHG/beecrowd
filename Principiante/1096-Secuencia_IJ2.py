i,j=1,7

while j>0:
    print(f'I={i} J={j}')
    j-=1
    if j==4:
        j+=3
        i+=2
    if i==11:
        break