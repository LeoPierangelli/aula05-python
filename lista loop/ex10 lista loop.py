#subtraindo
'''num = input('Digite o número desejado: ')
while not num.isnumeric():
    num = input('Digite o número desejado: ')
num = int(num)

aux = num - 1
while aux != 0:
    num = num * aux
    aux -= 1
print(num)
'''
# Somando:
i = 1
fatorial = 1
num = input('Digite um número: ')
while not num.isnumeric():
    num = input('Digite um número: ')

num = int(num)
while i <= num:
    fatorial *= i
    i += 1
print(fatorial)
