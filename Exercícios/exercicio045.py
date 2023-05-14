from random import randint
pc = randint(1, 3)
print('''Suas opções são:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada = int(input('Qual a sua jogada? '))
print(f'{pc}')
if jogada == 1:
    print('-=' * 10)
    print('O jogador jogou PEDRA')
    if pc == 1:
        print('O computador jogou PEDRA.')
        print('EMPATE')
    elif pc == 2:
        print('O computador jogou PAPEL')
        print('COMPUTADOR VENCE')
    elif pc == 3:
        print('O computador jogou TESOURA')
        print('JOGADOR VENCE')
if jogada == 2:
    print('O jogador jogou PAPEL')
    if pc == 1:
        print('O computador jogou PEDRA')
        print('JOGADOR VENCE')
    elif pc == 2:
        print('O computador jogou PAPEL')
        print('EMPATE')
    elif pc == 3:
        print('O computador jogou TESOURA')
        print('COMPUTADOR VENCE')
if jogada == 3:
    print('O jogador jogou TESOURA')
    if pc == 1:
        print('O computador jogou PEDRA')
        print('COMPUTADOR VENCE')
    elif pc == 2:
        print('O computador jogou PAPEL')
        print('JOGADOR VENCE')
    elif pc == 3:
        print('O computador jogou TESOURA')
        print('EMPATE')
print('-=' * 15)
