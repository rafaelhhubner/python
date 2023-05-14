v = int(input('O veículo estava se movendo a quantos Km por hora? '))
if v > 80:
    d = v - 80
    multa = d * 7
    print('Você ultrapassou a velocidade máxima permitida.')
    print(f'Você deverá pagar a multa de R${multa},00')
else:
    print('Tudo de acordo, tenha um bom dia!')
