from random import randint
print(26*'\033[1;31m==')
print('\033[1;30mVou pensar em um número entre 0 e 5. Tente adivinhar\033[m')
print(26*'\033[1;31m==')
number = int(input('\033[1;34mEm que número eu pensei? \033[m'))
number2 = randint(0, 5)
print(f'O  número que eu pensei foi {number2} ')
if number == number2:
    print('Parabéns você acertou!')
else:
    print('Que pena você errou! :c')
