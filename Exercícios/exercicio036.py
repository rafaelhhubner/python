v = float(input('Qual o valor da casa? '))
t = float(input('Em quantos anos pretende pagar? '))
r = float(input('Qual a sua renda mensal? '))
mes = t * 12
rd = r / 100 * 30
par = v / mes
if rd >= par:
    print('Empréstimo aprovado!')
    print(f'A prestação mensal será de R${round(par)},00')
elif rd < par:
    print('O empréstimo foi negado')
    
