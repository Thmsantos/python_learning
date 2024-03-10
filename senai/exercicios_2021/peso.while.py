altura = float (input ('Altura: '))
sexo = input ('masculino (m) - feminino (f)?: ')

while (sexo != 'f') and (sexo != 'm'):
    print ('sexo inválido!!')
    sexo = input ('masculino (m) - feminino (f)?: ')

if (sexo == 'm'):
        peso = (72.7 * altura) - 58
        print ('o peso ideal para sua altura é: ', peso)
elif (sexo == 'f'):
        peso = (62.1 * altura) - 44.7
        print ('o peso ideal para sua altura é: ', peso)
        

        
