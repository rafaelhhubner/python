from moeda import moeda
from dado import dado

num = dado.leiaDinheiro()
aum = str(input('Quer ver o aumento de quantos por cento? '))
if '%' in aum:
    aum.replace('%', '')
    aum = float(aum)
else:
    aum = float(aum)
dim = str(input('Quer ver a redução de quantos por cento? '))
if '%' in dim:
    dim.replace('%', '')
    dim = float(dim)
else:
    dim = float(dim)
res = str(input('Quer que os valores sejam formatados para a moeda Real (R$)? ')).strip().upper()[0]
if res not in 'NnSs':
    while True:
        print('ERRO. Digite SIM ou NÃO')
        res = str(input('Quer que os valores sejam formatados para a moeda Real (R$)? ')).strip().upper()[0]
        if res in 'NnSs':
            break
if res in 'Ss':
    r = True
else:
    r = False
moeda.resumo(num, aum, dim, r)
