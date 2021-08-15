exp = list(input('Digite uma expressão: '))
p = []
for s in exp:
    if s in exp:
        if s == '(':
            p.append('(')
        elif s == ')':
            if len(p) > 0:
                p.pop()
            else:
                p.append(')')
                break
if len(p) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
