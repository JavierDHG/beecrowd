N1, N2, N3, N4 = map(float, input().split())
N1 = (N1*2+N2*3+N3*4+N4*1)/10
print(f'Media: {N1:.1f}')
if N1 >= 7.0:
    print("Aluno aprovado.")
elif N1 < 5.0:
    print("Aluno reprovado.")
elif N1 >= 5.0 and N1< 7.0:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (N1+N)/2
    if N >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')