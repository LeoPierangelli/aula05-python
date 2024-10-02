num = input('Digite um número para verificar se ele é primo: ')
while not num.isnumeric():
    num = input('Digite um número para verificar se ele é primo: ')
num = int(num)

i = 2
while True:
    a = num % i
    i += 1

    if a == 0:
        print('Não é primo')
        break
    elif i >= num**(1/2):
        print('É primo')
        break