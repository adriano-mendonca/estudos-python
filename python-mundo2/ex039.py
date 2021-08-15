from datetime import date
year = int(input('Ano de nascimento: '))
ano = date.today().year
id = ano - year
print(f'Quem nasceu em {year} tem {id} anos em 2020.')
if id > 18:
    print(f'Você deveria ter se alistado há {id-18} anos.')
    print(f'Seu alistamento foi em {ano-(id-18)}.')
elif id == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif id < 18:
    print(f'Ainda faltam {18-id} anos para o alistamento.')
    print(f'Seu alistamento será em {18-id+ano}.')
