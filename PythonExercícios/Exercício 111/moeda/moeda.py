def mo(n):
    n = (f'R${n}').replace('.', ',')
    return n

def dobro(n, af = False):
    m = n * 2
    if af == True:
        o = f'{mo(m)}'
    else:
        o = m
    return o

def metade(n, af = False):
    m = n / 2
    if af == True:
        o = f'{mo(m)}'
    else:
        o = m
    return o

def aumentar(n, p, af = False):
    l = n / 100 * p
    m = n + l
    if af == True:
        o = f'{mo(m)}'
    else:
        o = m
    return o    

def diminuir(n, p, af = False):
    l = n / 100 * p
    m = n - l
    if af == True:
        o = f'{mo(m)}'
    else:
        o = m
    return o

def pou(n, af = False):
    if af == True:
        o = (f'{mo(n)}')
    else: 
        o = n
    return o

def linha(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))

def li(msg):
    print('-' * (len(msg) + 4))

def resumo(n, a, d, af = False):
    x = af
    linha('RESUMO DO VALOR')
    print(f'Valor analisado:  {pou(n, x)}')
    print(f'Dobro do preço:  {dobro(n, x)}')
    print(f'Metade do preço:  {metade(n, x)}')
    print(f'{a}% de aumento:  {aumentar(n, a, x)}')
    print(f'{d}% de redução:  {diminuir(n, d, x)}')
    li('RESUMO DO VALOR')