nome1 = 'Monica'
print (nome1.isalpha())
print('')

#contém espaço
nome2 = 'monica silva'
print (nome2.isalpha())
print('')

#contém numero
nome3= "m0nic4"
print (nome3.isalpha())
print('')

nome4 = "Monicasilva"

if nome4.isalpha() == True:
    print ('Todos caracteres são letras.')
else:
    print ('não são caracteres. ')
