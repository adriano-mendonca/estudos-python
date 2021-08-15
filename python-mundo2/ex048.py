cont = 0
tot = 0
for c in range(1, 500):
    if c % 2 != 0 and c % 3 == 0:
        cont += 1
        tot += c
print(f'A soma de todos os {cont} valores solicitados é {tot}')