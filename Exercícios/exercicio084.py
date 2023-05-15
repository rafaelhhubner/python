lista = []
lista1 = []
maior = menor = 0
while True:
    lista1.append(str(input('Nome: ')).strip())
    lista1.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = lista1[1]
    if lista1[1] > maior:
        maior = lista1[1]
    elif lista1[1] < menor:
        menor = lista1[1]
    lista.append(lista1[:])
    lista1.clear()
    resposta = str(input('Quer coninuar? [S/N]')).lower().strip()[0]
    if resposta in 'Nn':
        break

print(f'Ao todo, foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in lista:
    if c[1] == maior:
        print(f'{c[0]}', end=',')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end=',')
