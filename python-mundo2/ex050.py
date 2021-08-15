soma = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        soma += num
if soma != 0:
    print(f'A soma dos valores digitados pares é {soma}.')
else:
    print('Não foram digitados valores pares.')