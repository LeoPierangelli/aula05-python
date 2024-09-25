'''min = 0
max = 10
nota = int(input(f'Informe uma nota de {min} a {max}: '))
while not (nota >= min and nota <= max):
    nota = int(input('Digite um valor válido: '))
print(nota)'''

while True:
    num = input('Digite um número: ')
    if num.isnumeric():
        num = int(num)
        if num > 0 and num < 10:
            print('Boa')
            break

