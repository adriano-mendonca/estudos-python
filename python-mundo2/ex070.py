print(30*'\033[1;34m-\033[m')
print(f"\033[1;31m{'LOJAS AMERICANAS': ^30}\033[m")
print(30*'\033[1;34m-\033[m')
all = c = pb = cont = 0
nb = ''
while True:
    name = str(input('\033[30;1mNome do produto: ')).strip().capitalize()
    price = float(input('Preço: R$'))
    all += price
    cont += 1
    if price > 1000:
        c += 1
    if cont == 1:
        nb = name
        pb = price
    if pb > price:
        pb = price
        nb = name
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'\033[31;1m{" FIM DO PROGRAMA ":-^30}\033[m')
print(f'\033[30;1mO total ta compra foi R${all:.2f}')
print(f'Temos {c} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nb} que custa R${pb:.2f}')