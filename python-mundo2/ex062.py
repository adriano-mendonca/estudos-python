print(43*'\033[1;31m=')
print(8*'\033[1;33m-\033[m', '\033[1mG E R A D O R   D E   P A', 8*'\033[1;33m-')
print(43*'\033[1;31m=\033[m')
first = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
term = first
cont = 1
resp = 10
tot = 0
while resp != 0:
    tot += resp
    while cont <= tot:
       print(term, end=' -> ')
       term += razao
       cont += 1
    print('PAUSA')
    resp = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Foram exibidos {tot} termos.')