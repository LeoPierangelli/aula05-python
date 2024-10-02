i = 1
qtd = input('Digite a quantidade de notas que serão calculadas: ')
while not qtd.isnumeric():
    qtd = input('Digite a quantidade de notas que serão calculadas: ')

qtd = int(qtd)
notas = 0
while i <= qtd:
    num = input(f'Digite a {i}º nota: ')
    if num.isnumeric():
        num = int(num)
        i += 1
        notas += num

media = notas/qtd
print(f'A média das notas é: {media}')


