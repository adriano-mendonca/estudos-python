def contador(i, f, p):
    print(20*'-=')
    print(f'Contagem de {i} até {f} contando de {p} em {p} ')
    if p == 0:
        if f < 0:
            p = -1
        else:
            p = 1
    if f < 0 and p < 0:
        for c in range(i, f, +p):
            print(c, end=" ")
    elif i > f and p < 0:
        for c in range(i, f, -p):
            print(c, end=" ")
    else:
        for c in range(i, f+1, p):
            print(c, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(20*'-=')
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
