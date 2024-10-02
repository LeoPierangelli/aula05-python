soma = 0
i = 0
while i < 5:
    num = input('Digite um número: ')
    if num.isnumeric():
        num = int(num)
        i += 1
        soma = num + soma
    else:
        print('Digite um valor válido!')

media = soma/i
print(soma)
print(media)
