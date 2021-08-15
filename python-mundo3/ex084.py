temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] < menor:
            menor = temporaria[1]
        if temporaria[1] > maior:
            maior = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print(20*'-=')
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'O menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(p[0], end=' ')
print()
