d = dict()
d['nome'] = str(input('Nome: '))
d['média'] = float(input(f'Média de {d["nome"]}: '))
if d['média'] >= 7:
    d['situação'] = 'Aprovado'
elif d['média'] < 5:
    d['situação'] = 'Reprovado'
else:
    d['situação'] = 'Recuperação'
print(20*'=-')
for x, y in d.items():
    print(f' - {x} é igual a {y}')