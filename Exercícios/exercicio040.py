print('=' *25)
print('\033[30mCalculadora de Médias\033[m')
print('=' *25)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2) / 2
if m >= 7.0:
    print(f'\033[7;30mSua média é {m}\033[m')
    print('\033[34;40mAPROVADO\033[m')
elif m <= 6.9 and m >= 5.0:
    print(f'\033[7;30mSua média é {m}\033[m')
    print('\033[35;43mRECUPERAÇÃO\033[m')
else:
    print('\033[7;30mSua média é {m}\033[m')
    print('\033[31;46mREPROVADO\033[m')
