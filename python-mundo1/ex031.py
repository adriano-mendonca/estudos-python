distance = int(input('Qual vai ser a distância da sua viagem? '))
if distance <= 200:
    print(f'O preço da passagem será R${distance*0.5:.2f}')
else:
    print(f'O preço da passagem será R${distance*0.45:.2f}')