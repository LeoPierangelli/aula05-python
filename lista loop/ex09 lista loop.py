i = 0
pares = 0
while i < 10:
    num = input('Digite um número: ')
    if num.isnumeric():
        num = int(num)
        i += 1
        if num % 2 == 0:
            pares += 1
    else:
        print('Digite um valor válido!')

print(pares, 10 - pares)
