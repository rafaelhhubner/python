tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor',
             4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 24.9)
msg = f'LISTAGEM DE PREÇOS'
print('=' * (len(msg) + 21))
print(f'{"LISTAGEM DE PREÇOS":^37}'
)
print('=' * (len(msg) + 21))
m = 0
n = 1
a = 'R$'

for c in range(0, len(tupla)):
    if c % 2 == 0:
        print(f'{tupla[c]:.<30}', end='')
    else:
        print(f'R$ {tupla[c]:>6.2f}')
