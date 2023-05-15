resposta = maior = menor = soma = 0 
num = int(input('Digite um número inteiro: '))
maior = num
menor = num
soma = num
contador = 1
resposta = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
while resposta in 'Ss':
    print('\033[1m-\033[m' * 30)
    num = int(input('Digite um número inteiro: '))
    contador += 1
    soma += num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    média = soma / contador
    resposta = str(input('Você quer continuar? [S/N] ' )).strip().upper()[0]
    print('')
print(f'Você digitou {contador} números e a média entre eles foi {média}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
