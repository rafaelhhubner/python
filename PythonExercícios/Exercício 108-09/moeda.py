import coin

def metade(n, f=False):
    m = n / 2
    if f == True:
        p = f'{coin.moeda(m)}'
    else:
        p = m
    return p

def dobro(n, f=False):
    m = n * 2
    if f == True:
        p = f'{coin.moeda(m)}'
    else:
        p = m
    return p

def aumentar(n, p, f=False):
    m = n / 100 * p
    o = n+m
    if f == True:
        p = f'{coin.moeda(o)}'
    else:
        p = o
    return p 

def diminuir(n, p, f=False):
    m = n / 100 * p
    o = n - m
    if f == True:
        p = f'{coin.moeda(o)}'
    else:
        p = o
    return p
