f = str(input('Digite uma frase: ')).strip()
g = f.lower()
a = g.count('a')
b = g.find('a')+1
c = g.rfind('a')+1
print(f'A frase tem {a} letras "A" ')
print(f'O primeiro "A" está na posição {b}')
print(f'O último "A" está na posição {c}')