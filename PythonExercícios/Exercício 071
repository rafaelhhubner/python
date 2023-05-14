print('=' * 30)
print('        BANCO RANDOM')
print('=' * 30)
retirada = int(input('Qual valor você quer sacar? '))
contador50 = contador20 = contador10 = contador1 = 0
while True:
    if retirada >= 50:
        retirada -= 50
        contador50 += 1
    elif retirada < 50 and retirada >= 20:
        retirada -= 20
        contador20 += 1
    elif retirada < 20 and retirada >= 10:
        retirada -= 10
        contador10 += 1
    elif retirada < 10 and retirada >= 1:
        retirada -= 1
        contador1 += 1
    c1 = contador50 + contador20 + contador10 + contador1
    if retirada == 0:
        break
if contador50 > 0:
    print(f'Total de {contador50} cédulas de R$50')
if contador20 > 0:
    print(f'Total de {contador20} cédulas de R$20')
if contador10 > 0:
    print(f'Total de {contador10} cédulas de R$10')
if contador1 > 0:
    print(f'Total de {contador1} cédulas de R$1')
print(f'Ao todo {c1} cédulas foram retiradas')
print('Tenha um bom dia! Volte Sempre!')
