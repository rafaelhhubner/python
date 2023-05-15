print('\033[1m-\033[m' *25)
print('   CADASTRE UMA PESSOA')
print('\033[1m-\033[m' *25)
mdi = 0
homem = 0
mmv = 0
while True:
    idade = 0
    genero = 'a'
    idade = int(input('Idade: '))
    genero = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while genero not in 'MmFf':
        genero = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if genero in 'MmFf':
            break
    if genero in 'Mm':
        homem += 1
    if idade > 18:
        mdi += 1
    if genero in 'Ff' and idade < 20:
        mmv += 1
    resposta = str(input('Quer continuar? ')).strip().upper()[0]
    if resposta in 'Nn':
        break
print('=' * 5, end ='')
print('FINALIZADO', end ='')
print('=' * 5,)
print(f'Ao todo são {mdi} pessoas com mais de 18 anos')
print(f'Temos um total de {homem} homens')
print(f'E são {mmv} mulheres com menos de vinte anos.')
