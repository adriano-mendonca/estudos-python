n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1+n2)/2
print(f'Tirando {n1} e {n2}, a média do aluno é {med:.1f}')
if med < 5.0:
    print('O aluno está \033[31;1mREPROVADO\033[m.')
elif  med < 6.9 and med > 5.0:
    print('O aluno está de \033[34;1mRECUPERAÇÃO\033[m.')
else:
    print('O aluno está \033[1;32mAPROVADO\033[m.')
