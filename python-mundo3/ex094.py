cadastro = dict()
pessoas = list()
soma = 0
while True:
  cadastro.clear()
  cadastro['nome'] = str(input('Nome: ')).capitalize()
  while True:
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if cadastro['sexo'] in 'MF':
      break
    print('ERRO! Digite apenas M ou F!')
  cadastro['idade'] = int(input('Idade: '))
  soma += cadastro['idade']
  pessoas.append(cadastro.copy())
  while True:
    res = str(input('Quer continuar? [S/N] ')).upper()
    if res in 'SN':
      break
    print('ERRO! Digite apenas S ou N!')
  if res in "Nn":
    break
print(20*'-=')
media = soma / len(pessoas)
print(f'- Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram:', end=' ')
for m in pessoas:
  if m['sexo'] in 'F':
    print(f"{m['nome']}", end=" ; ")
print()
print('- A lista de pessoas acima da média:')
for p in pessoas:
  print('  ')
  for k, v in p.items():
    if p['idade'] > media:
      print(f'{k} = {v}', end=' ')
print('\n>> ENCERRADO <<')
