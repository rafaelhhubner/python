num = int(input('Digite um número inteiro [Digite 999 se quiser parar]: '))
contador = 1
soma = num
while True:
    num = int(input('Digite um número inteiro [Digite 999 se quiser parar]: '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Ao todo foram digitados {contador} números e a soma entre eles foi de {soma}')
