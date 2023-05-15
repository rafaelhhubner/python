contador = 0
lista = []
abc = 0
while True:
    num = int(input('Digite um Número Inteiro: '))
    contador += 1
    if num == 5:
        abc = 1
    if len(lista) == 0 or num < lista[-1]:
        lista.append(num)
    else:
        p = 0
        while True:
            if num > lista[p]:
                lista.insert(p, num)
                break
            p += 1
    res = str(input('Quer continuar? [Sim/Nao] ')).upper().strip()[0]
    if res in 'Nn':
        break  
print(f'Ao todo foram digitados {contador} valores')
print(f'Os valores em ordem decrescente: {lista}')
if abc > 0:
    print('O número 5 está na lista')
