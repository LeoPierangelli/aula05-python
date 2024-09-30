nome_usuario = input('Cadastre o seu nome de usuário: ')
while True:
    senha = input('Cadastre a sua senha: ')
    if senha == nome_usuario:
        print('A senha não pode ser igual ao nome de usuário!')
    else:
        break