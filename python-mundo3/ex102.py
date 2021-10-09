def fatorial(num, show=False):
    if show == True:
        for c in range(num, 0, -1):
            if c < num and  c > 0:
                print('x', end=' ')
            print(c, end=' ')
        print('= ', end='')
    for c in range(num-1, 0, -1):
        num = num * c
    return num

print(10*'---')
f = fatorial(5)
print(f)
