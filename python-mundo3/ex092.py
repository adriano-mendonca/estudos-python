from datetime import date
anoAtual = date.year
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['ctps'] != 0:
  cadastro['contratacao'] = int(input('Ano de Contratação: '))
  cadastro['salario'] = float(input('Salário: R$ '))
  cadastro['aposentadoria'] = 35 - (anoAtual - cadastro['contratacao']) + (anoAtual - cadastro['nascimento'])
  print(10*'-=')
  for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
else:
  print(10*'-=')
  for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
  
