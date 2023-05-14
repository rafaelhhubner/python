print('"' * 20)
ano = int(input('Em que ano você nasceu? '))
idade = 2022 - ano

print(f'Quem nasceu em {ano} tem {idade} anos em 2022.')
if idade < 18:
    diferença = 18 - idade
    print(f'\033[32mAinda faltam {diferença} anos para o seu alistamento\033[m.')
    print(f'O seu alistamento será em {2022 + diferença}.')
elif idade > 18:
    diferença = idade - 18
    print(f'\033[33mVocê já deveria ter se alistado há {diferença} anos\033[m.')
    print(f'O seu alistamento foi em {2022 - diferença}')
else:
    print('\033[1;31mVocê tem que se alistar IMEDIATAMENTE\033[m.')
