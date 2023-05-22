total = menor = contador = 0
print('=' *25)
print('        -CAIXA-')
print('=' *25)
produto = str(input('Nome do produto: ')).strip().capitalize()
preço = float(input('Preço: '))
menor = produto
menor1 = preço
total += preço
if preço > 1000:
    contador += 1
while True:
    print('=' * 25)
    res = str(input('Quer continuar adicionando produtos?')).strip().upper()[0]
    if res in 'Nn':
        break
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: R$ '))
    total += preço
    if preço < menor1:
        menor1 = preço
        menor = produto
    if preço > 1000:
        contador += 1
print(f'O total gasto com a compra foi de R${round(total/ 1,2)}')
print(f'Ao todo {contador} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {menor} que custa R${round(menor1/ 1,2)}')
print('-----FIM-----') 
