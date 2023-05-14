n = int(input('Qual o primeiro número desta Progressão Aritmética? '))
r = int(input('Qual é a razão desta Progressão Aritmética? '))
print(f'{n}', end ='')
for c in range(2, 11):

    n = n + (2 - 1) * r
    print('>', end ='')
    print(f'{n}', end ='')
