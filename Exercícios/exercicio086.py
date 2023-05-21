lista = []
for c in range(0, 9):
    lista.append(int(input('Digite um valor:')))
print('=' *30)
for c in range(0,9):
    if c == 2 or c == 5 or c == 8:
        print(f'[ {lista[c]} ]')
    else:
        print(f'[ {lista[c]} ]', end ='')
print('=' *30)
