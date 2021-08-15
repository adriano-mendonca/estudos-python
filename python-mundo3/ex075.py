conj = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'Você digitou os valores {conj}')
if 9 in conj:
    print(f'O valor 9 aparece {conj.count(9)} vezes.')
else:
    print(f'O valor 9 não aparece nenhuma vez.')
if 3 in conj:
    print(f'O valor 3 foi digitado na {conj.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for p in conj:
    if p % 2 == 0:
        print(p, end='')