lista = []
exp = str(input('Digite uma Expressão Matemática: '))
for c in exp:
    if c == ('('):
        lista.append(c)
    elif c == (')'):
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(c)
if len(lista) > 0:
    print('Expressão \033[1;31mINVÁLIDA\033[m')
else:
    print('Expressão \033[1;32mVÁLIDA\033[m')
