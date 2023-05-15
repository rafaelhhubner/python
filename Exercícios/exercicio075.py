tupla = (int(input('Digite um número inteiro: ')), 
        int(input('Digite um número inteiro: ')), 
        int(input('Digite um número inteiro: ')), 
        int(input('Digite um número inteiro: ')))
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro número 3 está na {tupla.index(3)+1}° posição')
else:
    print('Não há nenhum número 3.')
print(f'Os números pares foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
