from datetime import date


def voto(ano):
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos: voto NEGADO!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos: voto OPCIONAL!'
    elif idade >= 18 and idade < 60:
        return f'Com {idade} anos: voto OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: voto OPCIONAL!'


print(10*'---')
anoAtual = date.today().year
print(voto(int(input("Em que ano você nasceu? "))))
