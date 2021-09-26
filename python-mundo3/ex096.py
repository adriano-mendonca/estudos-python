def area(l, h):
    a = l * h
    print(f'A área de um terreno {l:.2f} x {h:.2f} é de {a:.2f}m².')


print(' Controle de Terrenos')
print(22*'-')
area(float(input('LARGURA (m):')), float(input('COMPRIMENTO (m): ')))
