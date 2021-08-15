peso = float(input('Qual é o seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso/(alt**2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
est = ' '
if imc <= 18.5:
    est = 'ABAIXO DO PESO'
elif imc > 18.5 and imc <= 25:
    est = 'PESO IDEAL'
elif imc > 25 and imc <= 30:
    est = 'SOBREPESO'
elif imc > 30 and imc <= 40:
    est = 'OBESIDADE'
else:
    est = 'OBESIDADE MÓRBIDA'
print(f'Seu estado: {est}')
