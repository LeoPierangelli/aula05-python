while True:
    num = input('Digite o numero do termo desejado: ')
    if num.isnumeric():
        num = int(num)
        break
    else:
        print('Insira um valor válido!')


i = 0
l = 0
t = 1
while i < num:
    aux = t + l
    t = aux + l
    l = t + aux
    i += 1

print(aux)