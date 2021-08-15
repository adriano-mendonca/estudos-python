valor = int(input('Valor da casa: R$'))
soldo = int(input('Salário do comprador: R$'))
years = int(input('Quantos anos de financiamento? '))
p = valor/(years*12)
print(f'Para comprar uma casa no valor de \033[1;30mR${valor}\033[m em \033[1;30m{years}\033[m anos a prestação será de \033[1;30mR${p:.2f}\033[m.')
if p >= soldo*0.3:
    print('O empréstimo foi \033[1;31mNEGADO\033[m!')
else:
    print('O empréstimo pode ser \033[1;34mCONCEDIDO\033[m!')
