i = 0
qtd_num = 5
while i > qtd_num:
    while True:
        numeros = input('Digite um número:')
        if numeros.isnumeric():
            numeros = int(numeros)
            soma += numeros
            media = soma/qtd_num
            i += 1
            break

    print(soma,media)
