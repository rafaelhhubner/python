dicionario = dict()
nome = str(input('Nome: '))
nasceu = int(input('Ano de Nascimento: '))
ct = int(input('Carteira de Trabalho (0 caso não tenha): '))
dicionario['Nome'] = nome
dicionario['Idade'] = 2022 - nasceu
dicionario['Carteira'] = ct
if ct != 0:
    ano = int(input('Ano de contratação:'))
    salario = float(input('Salário: '))
    dif = ano - nasceu
    aposenta = dif + 35
    dicionario['contratação'] = ano
    dicionario['Salário'] = salario
    dicionario['Aposentadoria'] = aposenta
print('=' *30)
for v in dicionario.items():
    print(f'- {v[0]} tem o valor {v[1]}')
print('Programa Encerrado')
