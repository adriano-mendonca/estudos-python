def leiaint(num):
    while True:
        numero = str(input(num))
        if numero.isnumeric() == False:
            while numero.isnumeric() == False:
                print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
                numero = str(input(num))
        return numero


print(15*'--')
n = leiaint('Digite um número: ')
print(f'\033[1;34mVocê acabou de digitar o número {n}.')
