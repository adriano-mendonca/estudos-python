from random import randint


def sorteio():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
    print('PRONTO!')


def soma():
    s = 0
    print('Somando os valores pares de', numeros, end=', ')
    for v in numeros:
        if v % 2 == 0:
            s+= v
    print('temos', s)


numeros = []
sorteio()
soma()
