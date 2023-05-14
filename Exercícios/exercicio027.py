n = str(input('Digite seu nome COMPLETO: ')).strip()
a = n.split()
print(f'O seu 1° nome é {a[0]}')
print(f'O seu 2° nome é {a[len(a)-1]}')
