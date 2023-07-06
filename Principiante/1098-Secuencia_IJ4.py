i,j=float(0),float(1)

for x in range(0,3):
    if i==0 and j==1:
        print(f'I={i:.0f} J={j+x:.0f}')
while i<=1.6:
    i+=0.2
    j+=0.2
    if (i//1!=i) and (j//1!=j):
        for x in range(0,3):
            print(f'I={i:.1f} J={j+x:.1f}')
    else:
        for x in range(0,3):
            print(f'I={i:.0f} J={j+x:.0f}')
for x in range(0,3):
            print(f'I={i:.0f} J={j+x:.0f}')
