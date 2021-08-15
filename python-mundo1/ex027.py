name = str(input('Digite seu nome completo: ')).strip().title().split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {name[0]}')
print(f'Seu último nome é {name[len(name) -1]}')