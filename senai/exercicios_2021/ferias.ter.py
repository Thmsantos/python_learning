#variáveis
ferias = int (input  ('O casal terá férias em dezembro? (1 - SIM) (2 - NÃO): '))
nota =  int (input ('Informe a nota de Carla: '))
salario = int (input ('O salário de maria ou marcos foi liberado antes do dia 12/12? (1 - SIM) (2 - NÃO): '))
diaria =int (input ('Informe o valor da diária: '))
compra_passagem =  float (input ('informe o dia da compra da passagem: '))
total = int (input ('informe o valor máximo a ser investido: '))
embarque = float (input ('informe o dia do embarque: '))
retorno = float (input ('Informe o dia do retorno: '))
passagem_tres = float (input ('Informe o valor da passagem: '))
cond = 0

#código
if (ferias == 1) :
    cond = cond +1
else:
    print ('não poderão viajar!!')
if (nota >= 7) and (nota <=10):
    cond = cond +1
else:
    print ('não poderão viajar!!')
if (salario == 1) :
    cond = cond +1
else:
    print ('não poderão viajar!!')

dias_passagem = embarque - compra_passagem

if dias_passagem < 10 :
    valor_passagem = (passagem_tres * 3) *2
    diaria_paga = retorno - embarque
    diariac = diaria * diaria_paga
    total_pago = diariac + valor_passagem
    cond = cond +1
else:
   
    valor_passagem = (passagem_tres * 3) *2
    diaria_paga = retorno - embarque
    diariac = diaria * diaria_paga
    total_pago = diariac + valor_passagem
    cond = cond +1

if (total_pago <= total) or (cond==4):
    print ('Boa viagem!!!!!!!!')
else:
    print ('Não poderão viajar!!')
    
