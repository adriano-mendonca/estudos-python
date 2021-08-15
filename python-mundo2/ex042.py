s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Os segmentos acima FORMAM um triângulo EQUILÁTERO.')
    elif s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2 or s2 == s3 and s2 != s1:
        print('Os segmentos acima FORMAM um triângulo ISÓSCELES.')
    else:
        print('Os segmentos acima FORMAM um triângulo ESCALENO.')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo.')