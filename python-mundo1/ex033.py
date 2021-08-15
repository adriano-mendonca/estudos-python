n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
menor = n1
maior = n2
if n2 < n1 and n2 < 3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')