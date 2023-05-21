from time import sleep
from operator import itemgetter
from random import randint
lista = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
classi = list ()
print('Valores Sorteados:')
for p, v in lista.items():
    print(f'{p} tirou {v} no dado')
    sleep(1)
classi = sorted(lista.items(), key=itemgetter(1), reverse=True )
print('=' *30)
print('          -\033[1mRANKING\033[m-')
for i, v in enumerate(classi):
    print(f'    {i+1}° Lugar: {v[0]} com {v[1]}]')
print('=' *30)
