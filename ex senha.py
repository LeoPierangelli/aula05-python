senha_cadastrada = '1234'
senha_input = input('Diga sua senha: ')
i = 1
mt = 5
#O while roda enquanto da false
while senha_cadastrada != senha_input and i < mt:
    #i = i + 1
    i += 1
    print(f'senha errada\n'
          f'tentativas restantes: {mt - i}')
    senha_input = input('Diga sua senha: ')

if senha_cadastrada == senha_input:
    print('Acesso liberado')
else:
    print('Pare')

