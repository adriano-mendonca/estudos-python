print(23*'\033[31;1m_')
print('\033[1;36mSEQUENCIA DE FIBONACCI')
print(23*'\033[1;31m-\033[m')
terms = int(input('\033[1;30mQuantos termos você quer ver? '))
cont = 1
t1 = 1
t2 = 1
print(60*'~')
print('0 -> 1 -> 1', end=' -> ')
cont = 3
while cont < terms:
    t3 = t1 + t2
    print(t3, end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print(60*'~')
