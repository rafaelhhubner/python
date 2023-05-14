import moeda

num = float(input('Digite um número: '))
aum = str(input('Quer aumentar em quantos por cento ?'))
dim = str(input('Quer diminuir em quantos por cento ?'))
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
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metede de {num} é {moeda.metade(num)}')
print(f'Aumentado {aum}%, temos {moeda.aumentar(num, aum)}')
print(f'Diminuindo {dim}%, temos {moeda.diminuir(num, dim)}')
