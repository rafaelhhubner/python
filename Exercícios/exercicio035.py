print('-' * 25)
print('Analisador de triângulos:')
print('-' * 25)
r1 = float(input('Digite o comprimento da 1° reta: '))
r2 = float(input('Digite o comprimento da 2° reta: '))
r3 = float(input('Digite o comprimento da 3° reta: '))
d1 = r1 + r2
d2 = r2 + r3
d3 = r3 + r1
if (d1 > r3) and (d2 > r1) and (d3 > r2):
    print('As retas citadas formam um triângulo')
else:
    print('NT NOIA')
