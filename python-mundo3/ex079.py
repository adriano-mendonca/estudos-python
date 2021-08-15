nums = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in nums:
        nums.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
print(f'Você digitou os valores: {nums}')