lista = list()
lista1 = list()
n = média = 0
m = 0
while True:
    nome = str(input('Digite o nome do aluno: ')).capitalize().strip()
    nota1 = float(input('Digite a 1° nota: '))
    nota2 = float(input('Digite a 2° nota: '))
    média = (nota1 + nota2) / 2
    lista1.append(nome)
    lista1.append(nota1)
    lista1.append(nota2)
    lista1.append(média)
    lista.append(lista1[:])
    lista1.clear()
    res = str((input('Quer continuar? [S/N]'))).strip().upper()[0]
    n += 1
    if res in 'Nn':
        break
print('=' *30)
print('No. Nome      Média')
print('-' *30)
for c in range(0, n):
    print(f'{c}  ', end='')
    print(f'{lista[m][0]}      ', end='')
    print(f'{lista[m][3]}')
    m += 1   
print('=' *30)
while True:
    r = int(input('Quer ver as notas de qual aluno? (999 para encerrar programa) '))
    if r == 999:
        break
    else:
        if r < len(lista) and len(lista) >= 0:
            print(f'As notas do aluno {lista[r][0]} foram {lista[r][1:3]}')
        else:
            print('Valor inválido, tente novamente.')
print('-' *30)
print('FIM DO PROGRAMA')
