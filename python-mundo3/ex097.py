def escreva(txt):
    print((len(txt)+2)*'~')
    print(f' {txt} ')
    print((len(txt)+2)*'~')

escreva(str(input('Digite a frase: ')))