while True:
    num = input('Digite um número para ver a tabuada: ')
    if num.isnumeric():
        num = int(num)
        break
    else:
        print('Digite um valor válido!')

print(f'Tabuada do {num}:')
i = 1
while i < 11 :
    print(f'{i} X {num} = {num*i}')
    i += 1