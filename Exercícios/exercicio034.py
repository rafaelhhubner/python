sal = float(input('Qual o salário atual do funcionário? '))
if sal > 1250:
    nov = sal + (sal / 100 * 10)
    print(f'O novo salário do funcionário será de R${nov}')
else:
    nov = sal + (sal / 100 * 15)
    print(f'O novo salário do funcionário será de R${nov}')
