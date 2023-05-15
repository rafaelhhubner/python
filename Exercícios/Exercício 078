lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]        
print('=' *30)
print(f'Você digitou {lista}')
print(f'O maior valor digitado foi {maior} que está na posição ', end='')
for l, q in enumerate(lista):
    if q == maior:
        print(f'{l}...')
print(f'O menor valor digitado foi {menor} que está na posição ', end='')
for l, q in enumerate(lista):
    if q == menor:
        print(f'{l}...')
print()
      