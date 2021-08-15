l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
cond = 'NÃO FORMAM'
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    cond = 'FORMAM'
print(f'Os segmentos informados {cond} um triângulo.')
