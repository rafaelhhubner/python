tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in tupla:
    print(f'\nNa palavra {c} temos ', end='')
    for v in c:
        if v.lower() in 'aeiou':
            print(v, end='')
 