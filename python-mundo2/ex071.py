print(20*'\033[1;30m==\033[m')
print(f"\033[1;33m{' CAIXA ELETRONICO ':-^40}")
print(20*'\033[1;30m==\033[m')
s = int(input('\033[1;32mQual valor você quer sacar? R$'))
c1 = c10 = c20 = c50 = 0
while True:
    if s // 50 != 0:
        while s // 50 != 0:
            c50 += 1
            s -= 50
        print(f'Total de {c50} cédulas de R$50')
    if s // 20 != 0:
        while s // 20 != 0:
            c20 += 1
            s -= 20
        print(f'Total de {c20} cédulas de R$20')
    if s // 10 != 0:
        while s // 10 != 0:
            c10 += 1
            s -= 10
        print(f'Total de {c10} cédulas de R$10')
    if s // 1 != 0:
        while s // 1 != 0:
            c1 += 1
            s -= 1
        print(f'Total de {c1} cédulas de R$1')
    print(20*'\033[1;30m==\033[m')
    break
print('Volte sempre ao nosso BANCO! Tenha um ótimo dia!')



