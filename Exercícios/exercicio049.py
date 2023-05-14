numero = int(input('Digite o número que deseja descobrir a tabuad: '))
cont = 0
for c in range(0,10):
    if numero >= -1:
        cont = cont + 1
        tabuada = numero * cont
    print(f'{numero} X {cont} = {tabuada}')

    