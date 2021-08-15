m = idm = idv = 0
for c in range(1, 5):
    print(f'------ {c} PESSOA ------')
    name = str(input('Nome: '))
    id = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper().strip()
    idm += id
    if id < 20 and sex == 'F':
        m += 1
    if idv < id and sex == 'M':
        idv = id
        nhv = name
print(f'A média de idade do grupo é de {idm/4:.1f} anos.')
print(f'O homem mais velho tem {idv} anos e se chama {nhv}.')
print(f'Ao todo são {m} mulheres com menos de 20 anos.')