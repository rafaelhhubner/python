p = float(input('Preço do produto: R$'))
print('''As formas de pagamento disponíveis são as seguintes:
[1] à vista em dinheiro/cheque.
[2] à vista no cartão
[3] em 2x no cartão   
[4] em 3x ou mais no cartão''')
r = int(input('Qual a opção escolhida, 1, 2,3 ou 4? '))
if r == 1:
    vp = p - (p / 100 * 10)
    print(f'O preço a ser pago é R${round(vp/1,2)}')
elif r == 2:
    vp = p - (p / 100 * 5)
    print(f'O preço a ser pago é R${round(vp/1,2)}')
elif r == 3:
    pd = p / 2
    print(f'O preço a ser pago é R${round(p/1,2)} dividido em 2 parcelas de {round(pd/1,2)}')
elif r == 4:
    vp = p + (p / 100 * 20)
    qp = int(input('Em quantas parcelas deseja pagar? '))
    dp = vp / qp
    print(f'O preço a pagar é R${round(vp/1,2)} dividido em {qp} parcelas de R${round(dp/1,2)}') 
else:
    print('Por favor escolha uma das 4 opções')
    r = int(input('Qual a opção escolhida, 1, 2,3 ou 4? '))
    if r == 1:
        vp = p - (p / 100 * 10)
        print(f'O preço a ser pago é R${round(vp/1,2)}')
    elif r == 2:
        vp = p - (p / 100 * 5)
        print(f'O preço a ser pago é R${round(vp/1,2)}')
    elif r == 3:
        pd = p / 2
        print(f'O preço a ser pago é R${round(p/1,2)} dividido em 2 parcelas de {round(pd/1,2)}')
    elif r == 4:
        vp = p + (p / 100 * 20)
        qp = int(input('Em quantas parcelas deseja pagar? '))
        dp = vp / qp
        print(f'O preço a pagar é R${round(vp/1,2)} dividido em {qp} parcelas de R${round(dp/1,2)}') 
