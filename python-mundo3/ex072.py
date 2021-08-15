ext = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        while True:
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
            if num <= 20 and num >= 0:
                break
    break
print(f'Você digitou o número {ext[num]}')