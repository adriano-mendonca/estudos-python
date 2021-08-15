c18 = ch = cm = 0
while True:
    print(21 * '-')
    print('   C A D A S T R O   ')
    print(21 * '-')
    id = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).upper().strip()
    if id > 18:
        c18 += 1
    if sex == 'M':
        ch += 1
    if sex == 'F' and id < 20:
        cm += 1
    print(21*'-')
    resp = str(input('Quer continuar? (S/N) ')).upper().strip()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {c18}')
print(f'Ao todo temos {ch} homens cadastrados.')
print(f'E temos {cm} mulheres com menos de 20 anos.')