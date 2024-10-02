numero1 = input('Digite o menor numero: ')
while not numero1.isnumeric():
    numero1 = input('Digite o menor numero: ')
numero1 = int(numero1)

numero2 = input('Digite o maior numero: ')
while not numero2.isnumeric():
    numero2 = input('Digite o maior numero: ')
numero2 = int(numero2)

if numero1 > numero2:
    aux = numero1
    numero1 = numero2
    numero2 = aux

while True:
    if numero1 == numero2-1:
        break
    numero1 += 1
    print(numero1)