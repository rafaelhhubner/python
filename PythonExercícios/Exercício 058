from random import randint
random = randint(0, 10)
guess = int(input('Digite um número de 0 a 10: '))
while guess != random:
    resposta = ('S')
    print('Sinto muito, você errou?')
    resposta = str(input('Gostaria de tentar novamente? ')).strip().upper()[0]
    if resposta == ('S'):
        guess = int(input('Digite um número de 0 a 10: '))
    else:
        guess = random
if resposta == ('S'): 
    print(f'Parabéns! Você acertou, o número realmente era {random}')
else:
    print('Perdedor')
