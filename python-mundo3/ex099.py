def maior(*num):
    print(10*'-=')
    print('Analisando os valores passados...')
    if len(num) == 0:
        maior = 0
    else:
        maior = num[0]
        for c in num:
            print(c, end=' ')
            if c > maior:
                maior = c
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
