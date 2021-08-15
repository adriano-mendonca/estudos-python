lc = list()
lp = list()
li = list()
while True:
    n = int(input('Digite um número: '))
    lc.append(n)
    if n % 2 == 0:
        lp.append(n)
    else:
        li.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break
print(20*'=-')
print(f'A lista completa é {lc}')
print(f'A lista de pares é {lp}')
print(f'A lisa de ímpares é {li}')
