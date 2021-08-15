ficha = []
while True:
    name = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1+n2)/2
    ficha.append([name, [n1, n2], med])
    r = str(input('Quer continuar? [S/N] '))
    if r in "Nn":
        break
print(20*'=-')
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(25*'-')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print(25 * '-')
    opt = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if opt == 999:
        print('FINALIZANDO...')
        break
    if opt <= len(ficha)-1:
        print(f'Notas de {ficha[opt][0]} são {ficha[opt][1]}')
print('<<< VOLTE SEMPRE >>>')
