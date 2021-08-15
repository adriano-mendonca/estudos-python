l = list()
while True:
    l.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N] ')).strip().upper()
    if r == 'N':
        break
print(20*'-=')
l.sort(reverse=True)
print(f'Você digitou {len(l)} elementos.')
print(f'Os valores digitados em ordem decrescente são {l}')
if 5 in l:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
