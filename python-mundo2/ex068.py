from random import randint
print(15*'=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(15*'=-')
c = 0
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    pc = randint(1, 10)
    s = n + pc
    print(20*'--')
    print(f'Você jogou {n} e o PC {pc}. Total de {s}', end=' ')
    if s % 2 == 0 and r == 'P':
        print('DEU PAR')
        print(20*'--')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        c += 1
    elif s % 2 != 0 and r == 'I':
        print('DEU ÍMPAR')
        print(20*'--')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        c += 1
    elif s % 2 != 0 and r == 'P':
        print('DEU ÍMPAR')
        print(20*'--')
        print('Você PERDEU!')
        break
    elif s % 2 == 0 and r == 'I':
        print('DEU PAR')
        print(20*'--')
        print('Você PERDEU!')
        break
    print(20*'=-')
print(20*'=-')
print(f'GAME OVER! Você venceu {c} vezes')