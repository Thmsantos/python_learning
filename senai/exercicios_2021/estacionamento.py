print ('----------------------------------------------------')
print ('SEJA BEM-VINDO AO THIAGO´S PARK!!!')
print ('----------------------------------------------------')
chegada = float ( input ('Horário de entrada: '))
saida = float (input ('Horário de saída: '))

if saida > chegada:
   tempo_uso = saida - chegada
else:
    tempo_uso = (24 - chegada) + saida
#calculo do preço    
if (tempo_uso >0) and (tempo_uso <3) :
    print ('Pague R$ 20.00')
elif (tempo_uso >=3) and (tempo_uso <=4):
    print ('Pague R$ 32.00')
else:
    hora_adc = tempo_uso - 4
    hora_paga = hora_adc * 8.00
    total = hora_paga + 32.00
    print ('Pague R$', total)
    
