A,B = map(int,input().split())
if A>=B:
    inicio = 24-A
    total = inicio+B
    print(f"O JOGO DUROU {total} HORA(S)")
elif B>A:
    total = B-A
    print(f"O JOGO DUROU {total} HORA(S)")