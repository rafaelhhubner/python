num = int(input('Digite um número inteiro: '))
print('=' *25)
print('Escolha uma das bases para conversão:')
print('[ 1 ] para binário')
print('[ 2 ] para octal')
print('[ 3 ] para hexadecimal')
print('=' * 25)
bc = int(input('Qual será sua opção? '))
if bc == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif bc == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif bc == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')

