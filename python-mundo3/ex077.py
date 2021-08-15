list = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
        'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in list:
    print(f'\nNa palavra {p} temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')
