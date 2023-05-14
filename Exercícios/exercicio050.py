s = 0
co = 0
for c in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
        co = co + 1
print(f'A soma entre os {co} números pares é {s}')

