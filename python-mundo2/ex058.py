from random import randint
pc = randint(0, 10)
print('''Olá Amigo! Sou seu computador...
Acabei de sortear um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
play = int(input('Qual é o seu palpite? '))
cont = 1
if play != pc:
    while play != pc:
        if play > pc:
            print('Menos... Tente mais uma vez.')
        else:
            print('Mais... Tente mais uma vez.')
        cont += 1
        play = int(input('Qual é o seu palpite? '))
print(f'Acertou com {cont} tentativas. Parabéns!')
