print(27*'=')
print('    10 TERMOS DE UMA PA    ')
print(27*'=')
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
for c in range(t, d, r):
    print(f'{c} -> ', end='')
print('Acabou!')
