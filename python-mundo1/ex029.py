vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[1;31mMULTADO! Você excedeu o limite pertido de 80km/h')
    print('Você deve pagar uma multa de \033[1;36mRS{:.2f}'.format(multa))
print('\033[1;32mTenha um bom dia! Dirija com segurança!')