#Essa é minha solução!
from random import randint
nums = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10)
print('Os números sorteados foram: ', end='')
maior = menor = nums[0]
for n in nums:
    print(n, end=' ')
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
#Solução do Guanabara!
'''print(max(nums))
print(min(nums))'''