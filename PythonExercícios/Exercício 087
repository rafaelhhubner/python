lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = 0
for p in range(0, 3):
    for q in range(0, 3):
        a = int(input(f'Digite uma valor para a posição {p} {q} '))
        if a % 2 == 0:
            par += a
        lista[p][q] = a
        if p == 1:
            if q == 0:
                maior = a
            else:
                if a > maior:
                    maior = a
for p in range(0, 3):
    for q in range(0, 3):
        if q == 2:
            print(f'[ {lista[p][q]} ]')
        else:
            print(f'[ {lista[p][q]} ]', end = '')
print(f'A soma de todos os números pares digitados é: {par}')
print(f'A soma de todos os valores da 3° coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é {maior}')
