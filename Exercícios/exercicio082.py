lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r in 'Nn':
        break
print('=' *30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é : {impar}')
