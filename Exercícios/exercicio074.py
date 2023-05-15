from random import randint
n1 = n2 = n3 = n4 = n5 = maior = menor = 0
for c in range(1,6):
    r = randint(1,10)
    if c == 1:
      n1 = r
      maior = r
      menor = r
    elif c == 2:
      n2 = r
    elif c == 3:
       n3 = r
    elif c == 4:
       n4 = r
    elif c == 5:
       n5 = r
    if menor > r:
       menor = r
    if maior < r:
       maior = r
#tupla = (f'{n1}', f'{n2}', f'{n3}', f'{n4}', f'{n5}')
tupla = (n1, n2, n3, n4, n5)
print(tupla)
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
