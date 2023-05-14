a = 0
hmv = ('o')
ihmv = 0
mva = 0
it = 0
for c in range(0,4):
    a = a + 1
    print(f'\033[1m----- {a}° Pessoa -----\033[m')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    gênero = str(input('Sexo [M/F]: ')).upper().strip()
    it = it + idade
    if gênero == ('F') and idade < 20:
        mva = mva + 1
    elif gênero == ('M') and idade > ihmv:
        hmv = nome
        ihmv = idade
    media = it / 4
print('')
print(f'A média de idade do grupo é {media} anos.')
print(f'O homem mais velho tem {ihmv} e se chama {hmv}.')
print(f'Ao todo são {mva} mulheres com menos de 20 anos.')

    

         
