print(43*'\033[1;33m=')
print(8*'\033[1;31m-\033[m', '\033[1mG E R A D O R   D E   P A', 8*'\033[1;31m-')
print(43*'\033[1;33m=')
t1 = int(input('\033[1;34mPrimeiro termo: '))
r = int(input('Razão: \033[1;36m'))
c = 0
while c < 10:
    print(t1, end=' -> ')
    t1 += r
    c += 1
print('FIM')
