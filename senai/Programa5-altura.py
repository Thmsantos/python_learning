
metros = float ( input ('Informe sua altura: '))
cm = metros * 100
genero = int ( input ('Sexo: 1 = masculino ou 2 = feminino:'))
if  genero == 1 : 
    peso = (cm - 100) * 0.90
    print ('seu peso ideal é: ',peso)
elif genero == 2 :
    peso = (cm -100) * 0.85
    print ('seu peso ideal é: ',peso)
    
