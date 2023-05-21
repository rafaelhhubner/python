from random import randint
print('=' *30)
print('      JOGUE NA MEGA-SENA')
print('=' *30)
lista = list()  
verdade = list()
a = 1
pessoa = int(input('Quantos sorteios quer realizar? '))
while a <= pessoa:
    contador = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    verdade.append(lista[:])
    lista.clear()
    a += 1
print('=' *30)
for c, l in enumerate(verdade):
    print(f'Jogo {c+1}: {l}')
