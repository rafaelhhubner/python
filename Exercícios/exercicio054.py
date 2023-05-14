a = 0
men = 0
mai = 0
for c in range(0,7):
    a = a + 1
    ano = int(input(f'Em que ano a {a}° pessoa nasceu? '))
    idade = 2022 - ano
    if idade >= 18:
        mai = mai +1
    elif idade < 18:
        men = men + 1
print(f'Ao todo tivemos {mai} pessoas maiores de idade.')
print(f'Ao todo tivemos {men} pessoas menores de idade')