from time import sleep

def contador(i, f, p):
    print(20*'-=')
    print(f'Contagem de {i} até {f} contando de {p} em {p} ')
    for c in range(i, f+1, p):
        print(c, end=' ')
        #sleep(1)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(20*'-=')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

if inicio > fim:
    passo = passo*(-1)
    if passo == 0:
        passo = 1
    contador(fim, inicio, passo)
