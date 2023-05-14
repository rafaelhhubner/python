lis = list()
dicio = dict()
zoro = list()

def linha(msg, aum):
    print('=' * (len(msg) + aum))
    print(f'{msg:^38}')
    print('=' * (len(msg) + aum))

def lista(a):
    lis.append(a)

def dicionario(a, b):
    dicio['Nome'] = a
    dicio['Idade'] = b

def limpa():
    dict.clear()
    list.clear()

def printl(a, b, af = False):
    if af == False:
        print(f"{lis[a][f'{b}']:<20}", end='')
    else:
        print(f"{lis[a][f'{b}']:>6} Anos")


def printd():
    print(dicio)

