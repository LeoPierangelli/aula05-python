'''nome = input('Nome: ')
while len(nome) <= 3:
    nome = input('Insira um nome com mais de 3 caracteres: ')
idade = int(input('Idade: '))
while not (idade > 0 and idade <150):
    idade = int(input('Insira um valor válido: '))
salario = float(input('Digite o seu salário: '))
while salario < 0:
    salario = float(input('Insira um valor válido:'))
sexo = input('Digite o seu sexo ("f" ou "m"): ')
while not (sexo == 'f' or sexo == 'm'):
    sexo = input('Insira um valor válido: ')
estado_civil = input('Digite o seu estado civil: ')
while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd'):
    estado_civil = input('Insira um valor válido: ')

print('fim')'''

nome = input('Nome: ')
while len(nome) <= 3:
    nome = input('Insira um nome com mais de 3 caracteres: ')

while True:
    idade = input('Idade: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        else:
            print('Apenas valores entre 0 e 150!')
    else:
        print('Apenas números serão aceitos!')

salario = input('Diga seu salário: ')
while not salario.isnumeric():
    salario = input('Insira um valor válido: ')
salario = float(salario)

sexo = input('Diga o seu sexo (f para feminino e m para masculino): ')
while not (sexo == 'f' or sexo == 'm'):
    sexo = input('Digite um valor válido: ')

ec = input('Diga seu estado civil(s,c,v ou d): ')
while not (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
    ec = input('Diga seu estado civil (use apenas s,c,v ou d): ')

print('fim')

