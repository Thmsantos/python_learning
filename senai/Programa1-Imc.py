#variaveis
peso =  float ( input ('Informe seu peso: '))
altura =  float (input ('Informe sua altura: '))
imc =  peso/ (altura**2)

#algorítimo

if imc < 16:
 print ('O imc de ', imc,  ' é de baixo peso muito grave!')
elif imc >=16 and imc <16.9:
   print ('O imc de', imc, ' é de baixo peso grave!')
elif imc  >= 17  and imc <18.5:
   print ('O imc de', imc, ' é de baixo peso!')
elif imc >=18.5 and imc <24.9:
   print ('O imc de', imc,' é normal!')
elif imc >=24.9 and imc <29.9:
   print ('O imc de', imc,' é  sobrepeso!')
elif imc >=30 and imc <34.9:
   print ('O imc de', imc,' é de obesidade nível 1!')
elif imc >=35 and imc <39.9:
   print ('O imc de', imc,' é de obesidade nível 2!')
elif imc >= 40:
   print ('O imc de', imc,' é de obesidade mórbida!') 
