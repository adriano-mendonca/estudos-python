def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional, para mostrar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    nota = dict()
    nota['total'] = len(n)
    maior = menor = n[0]
    soma = 0
    for c in n:
        soma += c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    nota['maior'] = maior
    nota['menor'] = menor
    nota['média'] = soma/len(n)

    if sit is True:
        if nota['média'] > 7:
            nota['situação'] = 'Aprovado'
        else:
            nota['situação'] = 'Recuperação'
    return nota


resp = notas(5.5, 9.5, 10, 6.5, 10, 10, 10, sit=True)
print(resp)
