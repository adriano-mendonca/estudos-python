from datetime import date
hj = date.today().year
contm1 = 0
contm2 = 0
for c in range(1, 8):
    year = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if hj - year >= 18:
        contm1 += 1
    elif hj - year < 18:
        contm2 += 1
print(f'Ao todo tivemos {contm1} pessoas maiores de idade.\nE também tivemos {contm2} pessoas menores de idade.')