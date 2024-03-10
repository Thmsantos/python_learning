valor = float ( input ('Valor da compra: '))
parcelas = int ( input ('Número de parcelas (se for a vista digite 1) : '))
idade = int (input ('Idade: '))
cliente = int (input ('quantos anos que é cliente da loja ABC: '))

#método1
if (parcelas == 1):
    descontoc = 10
elif (parcelas > 1) and (parcelas <=6):
    descontoc = 5
elif (parcelas >6):
    
    descontoc = 0


#método2
if (valor >= 5000):
    descontob = 5

else:
    descontob = 0

if (idade >= 60):
    descontob = descontob + 5
else:
    descontob = 0 + descontob

if (cliente >= 10):
    descontob = descontob + 5
else:
    descontob = 0 + descontob
 

desconto = descontob + descontoc
percentual_desconto = (desconto * valor) / 100
valor_totalb = percentual_desconto - valor
valor_total = valor_totalb * -1
parcela =  valor_total / parcelas
print ('O valor do desconto foi de :', percentual_desconto, '. O valor com o desconto ficou: ', valor_total, ', O valor das parcelas ficaram em: ',parcela,'!')





    
