txt = str(input('Digite uma frase: ')).upper().strip()
sp = txt.split()
jt = ''.join(sp)
palin = jt[::-1]
print(f'O inverso de {jt} é {palin}')
if palin == jt:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')