tu = 0
print('\033[1;35mCalculadora de Números Primos\033[m')
num = int(input('Digite um Número Inteiro: '))
for c in range(1, num + 1):
    print(' ', end='')
    if num % c == 0:      
        print(f'\033[33m{c}\033[m', end='')
        tu += 1
    else:
        print(f'\033[31m{c}\033[m', end='')
print('')
print(f'O número {num} é divisível {tu} vezes.')
if tu == 2:
    print('E por isso ele é \033[4;34;40mPRIMO\033[m', end='')
else:
    print('E por isso, ele \033[1;35;41mNÃO\033[m é primo', end='')
