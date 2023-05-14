print('=' * 20)
print(' Inversor de Frases')
print('=' * 20)
frase = str(input('Digite aqui uma frase qualquer: ')).strip().upper().replace(' ', '')
esarf = frase.strip().upper().replace(' ', '')[:: -1]
print(f'{esarf}')
if frase == esarf:
    print('E é um PALÍNDROMO')
else:
    print('E não é um PALÍNDROMO')
