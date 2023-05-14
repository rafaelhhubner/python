import moeda

def moeda(n, local='R$'):
    a = f'{local}{n}'.replace('.', ',')
    return a

