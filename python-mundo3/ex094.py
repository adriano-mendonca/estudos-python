cadastro = dict()
cadastroLista = list()
contador = 0
idades = 0
mulheres = list()
acimaMedia = list()
while True:
  cadastro['nome'] = str(input('Nome: ')).capitalize()
  cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
  cadastro['idade'] = int(input('Idade: '))
  contador += 1
  idades += cadastro['idade']
  cadastroLista.append(cadastro.copy())
  if cadastro['sexo'] in "Ff":
    mulheres.append(cadastro['nome'])
  resposta = str(input('Quer continuar? [S/N] '))
  if resposta in 'Nn':
    break
mediaIdades = idades/contador
print(15*'-=')
print(f'- O grupo tem {contador} pessoas.')
print(f'- A média de idade é de {mediaIdades:.2f} anos.')
print('- As mulhes cadastradas foram:', end=' ')
for c in mulheres:
	print(c, end='; ')
print()
print('- Lista das pessoas que estão acima da média:')
for p in range(0, len(cadastroLista)):
	if cadastroLista[p]['idade'] > mediaIdades:
		acimaMedia.append(cadastroLista[p])
for x in range(0, len(acimaMedia)):
	for k, v in acimaMedia[x].items():
		print(f'{k} = {v}', end= ' ; ')
print()
print('\n>> ENCERRADO <<')
