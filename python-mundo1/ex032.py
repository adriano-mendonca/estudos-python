print(' VERIFICADOR  DE  ANO  BISSEXTO')
year = int(input('Qual ano você quer ver se é bissexto? '))
if year % 4 == 0:
    print(f'O ano {year} é um ano bissexto!')
else:
    print(f'O ano {year} não é um ano bissexto!')