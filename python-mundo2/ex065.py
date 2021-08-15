n = int(input('Digite um número: '))
resp = str(input('Quer continuar? [S/N] ')).strip()
tot = maior = menor = n
cont = 1
while resp not in 'Nn':
    cont += 1
    n = int(input('Digite um número: '))
    tot += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar? [S/N] '))
print(f'Você digitou {cont} números e a média foi {tot/cont:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')