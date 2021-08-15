nums = list()
for c in range (0, 5):
    nums.append(int(input(f'Digite um valor para a posição {c}: ')))
print(20*'=-')
print(f'Você digitou os valores: {nums}')
print(f'O maior valor digitado foi {max(nums)} nas posições: ',end='')
for p, n in enumerate(nums):
    if n == max(nums):
        print(f'{p}...', end=' ')
print(f'\nO menor valor digitado foi {min(nums)} nas posições: ', end='')
for p, n in enumerate(nums):
    if n == min(nums):
        print(f'{p}...', end=' ')