tamanho = int(input('numero de caracteres da senha: '))

from random import randint
loop = True
while loop:
    print('-------------------')
    print('GERADOR DE SENHAS')
    print('[1] - Nova Senha')
    print('[2] - Encerrar')
    escolha = int(input('selecione uma opção: '))
    if escolha == 1:
        inicial = int(input('número inicial: '))
        final = int(input('número final: '))
        for senha in range(0, tamanho):
            novaSenha = randint(inicial , final)
            print(novaSenha)
    elif escolha == 2:
        break
    else:
        print('Opção inválida')

