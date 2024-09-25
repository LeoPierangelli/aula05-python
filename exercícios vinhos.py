vinho1 = 'Chapinha'
vinho2 = 'Pérgola'
vinho3 = 'Catuaba'

'''a = input('Escolha o seu vinho: ')
while a != vinho1 and a != vinho2 and a != vinho3:
    a = input('Digite uma das opções válidas: ')

if a == vinho1 or a == vinho2 or a == vinho3:
    print('Boa')'''

a = input('Escolha o seu vinho: ')
while not (a == vinho1 or a == vinho2 or a == vinho3):
    a = input('Digite uma das opções válidas: ')

if a == vinho1 or a == vinho2 or a == vinho3:
    print('Boa')
    