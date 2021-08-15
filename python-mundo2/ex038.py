n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 == n2:
    print('Os dois valores são \033[32;1mIGUAIS\033[m!')
elif n1 > n2:
    print('O primeiro valor é \033[34;1mMAIOR\033[m!')
elif n1 < n2:
    print('O segundo valor é \033[34;1mMAIOR\033[m!')
