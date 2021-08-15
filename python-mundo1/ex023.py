number = int(input('Digite um número de até 4 algarismos: '))
print(f'Analisando o número {number} ...')
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')