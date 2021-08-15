s = int(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    print(f'O seu salário subiu de {s} para R${s*1.1:.2f}')
else:
    print(f'O seu salário subiu de {s} para R${s*1.15:.2f}')
