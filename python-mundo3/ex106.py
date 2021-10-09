def centro(txt, c):
    print(f'\033[1;{c}m', end='')
    print(len(txt)*'~')
    print(f'{txt}')
    print(len(txt) * '~')
    print('\033[m', end='')

def ajuda(x):
    centro(f" Acessando o manual do comando '{x}' ", 44)
    print('\033[40;39;1m', end='')
    help(x)


while True:
    centro('  SISTEMA DE AJUDA PyHELP  ', 42)
    r = input('\033[mFunção ou Biblioteca > ')
    if r.upper() == 'FIM':
        break
    ajuda(r)
centro(' ATÉ LOGO! ', 41)
