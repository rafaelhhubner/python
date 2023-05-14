def leiaDinheiro():
    while True:
        a = str(input('Digite um valor: ')).replace('.', ',').strip()
        if a.isalpha() == True or a == '':
            print('\033[1;31mERRO. Você deve digitar o valor como um NÚMERO INTEIRO\033[m')
        else:
            a = float(a)
            break
    return a
