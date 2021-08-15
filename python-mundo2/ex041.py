from datetime import date
year = int(input('Ano de nascimento: '))
ano = date.today().year
id = ano - year
print(f'O atleta tem {id} anos.')
clas = 'nada'
if id <= 9:
    clas = 'MIRIM'
elif id > 9 and id <= 14:
    clas = 'INFANTIL'
elif id > 14 and id <= 19:
    clas = 'JUNIOR'
elif id > 19 and id <= 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'
print(f'Classificação: {clas}')