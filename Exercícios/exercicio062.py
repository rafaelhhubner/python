print('Gerador de Progressão Aritmética')
print('=' * 25)
pt = int(input('Qual o Primeiro Termo da PA? '))
ra = int(input('Qual a Razão da PA? '))
contador = 0
total = -1
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        contador = contador + 1
        print(f'{pt}', end='')
        pt = pt + ra
        if total >= contador:
            print(f' -> ', end='')
        else:
            print(' PAUSA ')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Fim da Progressão. {contador} termos foram mostrados.')
