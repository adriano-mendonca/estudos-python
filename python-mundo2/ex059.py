n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
op = 0
while op != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novo Números
[5] Sair do programa''')
    op = int(input('>>>>>> Qual é a sua opção? '))
    if op > 5:
        print('Opção inválida, tente novamente!')
    elif op == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}')
        else:
            print(f'Entre {n1} e {n2} o maior é {n2}')
    elif op == 4:
        print('Informe os números novamente!')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um valor: '))
    print(10 * '===')
print('Fechando o programa...')