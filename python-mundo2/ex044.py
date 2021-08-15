price = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))
if option == 1:
    print(f'Valor da compra: R${price * 0.9:.2f}')
elif option == 2:
    print(f'Valor da compra: R${price*0.95:.2f}')
elif option == 3:
    print(f'Valor da compra: R${price:.2f}')
elif option == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Valor da compra: R${price * 1.20:.2f} em {parcelas}x de R${(price*1.20)/parcelas:.2f}')
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')