while True:
    num = input('Digite o numero do termo desejado: ')
    if num.isnumeric():
        num = int(num)
        break
    else:
        print('Insira um valor válido!')

a = 0
b = 1
i = 1
print(f'1ºnúmero: {b}')
while num > i:
    c = a + b
    a = b
    b = c
    i += 1
    print(f'{i}ºnumero: {c}')
