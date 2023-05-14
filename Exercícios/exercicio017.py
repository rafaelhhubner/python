from math import hypot
print('Quer saber o comprimento da Hipotenusa de um triângulo? ')
co = float(input('Qual o comprimento do Cateto Oposto deste triângulo? '))
ca = float(input('Qual o comprimento do Cateto Adjacente deste triângulo? '))
h = hypot(co, ca)
print(f'A hipotenusa deste triângulo é {h}')
