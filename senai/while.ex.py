login = input ('Login: ')
senha = input ('Digite a senha: ')

while (login == senha):
    print (' sua senha deve ser diferente do login. tente novamente ')
    senha = input ('informe a senha: ')

print ('Ok. Login e senha válidos!')
