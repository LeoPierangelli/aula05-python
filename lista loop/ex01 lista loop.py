min = 0
max = 10
nota = int(input(f'Informe uma nota de {min} a {max}: '))
while not (nota >= min and nota <= max):
    nota = int(input('Digite um valor válido: '))
print(nota)