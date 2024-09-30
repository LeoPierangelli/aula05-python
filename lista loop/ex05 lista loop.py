i = 0
b = 10
while i < b:
    numero1 = input('Digite o menor numero: ')
    if numero1.isnumeric():
        numero1 = int(numero1)
        while i < b:
            numero2 = input('Digite o maior numero: ')
            if numero2.isnumeric():
                numero2 = int(numero2)
                while numero1 < numero2-1:
                    numero1 += 1
                    b = numero2
                    i += 2
                    print(numero1)
            else:
                print('Digite um valor válido!')
    else:
        print('Digite um valor válido!')
