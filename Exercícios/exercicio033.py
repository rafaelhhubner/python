n1 = int(input('Digite aqui um número: '))
n2 = int(input('Digite aqui outro número: '))
n3 = int(input('Digite enfim, um último número: '))
m = [n1, n2, n3]
m.sort()
print(f'O menor número é {m[0]}')
print(f'O maior número é {m[2]}')
