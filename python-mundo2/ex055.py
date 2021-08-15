maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')