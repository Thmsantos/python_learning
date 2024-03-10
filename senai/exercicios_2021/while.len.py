nome = str (input ('informe o seu nome (maior que 3 caracteres) : '))

while (len (nome) <3):
    print  ('NOME INVÁLIDO!!! Informe um nome válido: ')
    nome = str (input ('Nome: '))

idade = int (input ('idade: '))

while (idade < 1) or (idade > 200):
    print  ('IDADE INVÁLIDA!!! Informe uma idade válida: ')
    idade = int (input ('idade: '))

salario = float (input ('seu salário: '))

while (salario <= 0):
    print ('informe um salário váildo!')
    salario = float (input ('salario: '))

sexo = input ('masculino (m) ou feminino (f)? ')

while (sexo != 'f') and (sexo != 'm'):
    print ('informe um sexo válido!')
    sexo = input ('sexo: ')

estado_civil = input ('solteiro  - casado  - viuvo  - divorciado - enrolado?: ')

while (estado_civil != 'solteiro') and (estado_civil != 'casado') and (estado_civil != 'viuvo') and (estado_civil != 'divorciado') and (estado_civil != 'enrolado')  :
    print ('informe o seu estado civil correto!!')
    estado_civil = input ('solteiro  - casado  - viuvo  - divorciado - enrolado: ')


print ('-----------------------')
print ('o(a) : ', nome)
print ('de: ', idade,'anos')
print ('recebe: ', salario, '00')
print ('do sexo: ', sexo)
print ('está: ' , estado_civil)
