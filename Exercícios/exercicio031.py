km = int(input('Qual a distância da viagem em Km? '))
if km <= 200:
    tarifa = km * 0.5
    print(f'O valor da tarifa será R${tarifa}')
else:
    tarifa = km * 0.45
    print(f'O valor da tarifa será R${tarifa}')
