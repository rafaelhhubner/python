n = int(input('Digite um número: '))
z = n
y = 1
print(f'Calculando {n}! = ', end ='')
while z > 0:
    print(f'{z}', end='')
    print(' X ' if z > 1 else ' = ', end='')
    y = y * z
    z = z - 1
print(f'{y}')
