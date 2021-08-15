from math import factorial
num = int(input('Digite um número para\ncalcular seu fatorial: '))
print(f'Calculando {num}! = ', end='')
c = num
f = 1
while c > 0:
    print(f'{c} ', end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)