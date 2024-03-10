salario = float(input('Salário: '))

if (salario <= 980):
   aumentop = (salario * 20) / 100
   percentual = 20
   aumento = aumentop + salario
elif (salario >= 981) and (salario <=  1700):
    aumentop =  (salario * 15) / 100
    percentual = 15
    aumento = aumentop + salario
elif (salario >= 1701) and (salario <= 2500):
    aumentop =  (salario * 10) /100
    percentual = 10
    aumento = aumentop + salario
else:
    aumentop =  (salario * 5) /100
    percentual = 5
    aumento = aumentop + salario
    
print ('O salário era de: ', salario, '. Com o reajuste de ', percentual,'%, que tem valor de ', aumentop, 'o salário ficou: ', aumento)
    
