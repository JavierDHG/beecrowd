i,j=1,7

while j>0:
    print(f'I={i} J={j}')
    j-=1
    if i==1 and j==4 or i==3 and j==6 or i==5 and j==8 or i==7 and j==10:
        j+=5
        i+=2
    if i==9 and j==12:
        break