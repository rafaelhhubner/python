import moeda
import coin

num = float(input('Digite um número: '))
aum = str(input('Quer aumentar em quantos por cento ?'))
dim = str(input('Quer diminuir em quantos por cento ?'))
while True:
    res = str(input('Quer a formatação dos valores em Real(R$) [Sim/Não] ?')).upper().strip()[0]
    if res in 'NnSs':
        break
    else: 
        print('ERRO.Você precisa responder com "\033[1;32mSIM\033[m" ou "\033[1;31mNÃO\033[m"')
if res in 'Nn':
    af = False
elif res in 'Ss':
    af = True
if '%' in aum:
    aum.replace('%', '')
    aum = aum(aum)
else:
    aum = float(aum)
if '%' in dim:
    dim.replace('%', '')
    dim = float(dim)
else:
    dim = float(dim)
print(f'O dobro de {coin.moeda(num)} é {moeda.dobro(num, af)}')
print(f'A metede de {coin.moeda(num)} é {moeda.metade(num, af)}')
print(f'Aumentado {aum}%, temos {moeda.aumentar(num, aum, af)}')
print(f'Diminuindo {dim}%, temos {moeda.diminuir(num, dim, af)}')
