n = cont = tot = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    tot += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont-1} números e a soma entre eles é {tot-999}.')
