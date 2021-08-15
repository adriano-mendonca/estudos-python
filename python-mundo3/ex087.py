matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = maior = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(20*'-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if c == 2:
            sc += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]
    print()
print(20*'-=')
print(f'A soma dos valores pares é {sp}.')
print(f'A soma dos valores da terceira coluna é {sc}.')
print(f'O maior valor da segunda linha é {maior}.')