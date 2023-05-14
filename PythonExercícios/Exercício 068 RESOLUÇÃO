from random import randint
print('=' * 25)
print('Par ou Ímpar, ser perder o jogo acaba.')
print('=' * 25)
contador = 0
while True:
    jogador = int(input('Digite um valor: '))
    escolha = ' '
    pc = randint(0, 10)
    total = pc + jogador
    total1 = total % 2
    resultado = 0
    resultad0 = 'a'
    while escolha not in 'IP':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if total1 == 0:
        resultado = ('P')
        resultad0 = ('PAR')
    elif total1 != 0:
        resultado = ('I')
        resultad0 = ('ÍMPAR')
    if escolha == resultado:
        contador += 1
        print(f'O computador jogou {pc}, você jogou {jogador}, o que resulta em {total} que é {resultad0}')
        print('Você ganhou.')
    elif escolha != resultado:
        print(f'O computador jogou {pc}, você jogou {jogador}, o que resulta em {total} que é {resultad0}')
        print('O Computador ganhou')
        break
print(f'A partida acabou, e você ganhou {contador} vezes. ')

