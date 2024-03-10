n = 0

while  True:

    n = int (input ('deseja continuar? (0 sim) (1 não) : '))

    if n == 1:
            break

    dias = int (input ('quantos dias trabalha por mês? : '))
    horas = int (input ('Quantas horas trabalha por dia: '))
    salario = int (input ('informe seu salário: '))
    ganho_hora = (salario/dias) / horas
    imp_renda = (salario * 11) / 100
    inss = (salario * 8) / 100
    sindicato = (salario * 5) / 100 
    descontos = inss + imp_renda + sindicato
    salario_lq = salario - descontos
    


    print ('recebe', ganho_hora, 'por hora')
    print ('o salario bruto é : ',salario)  
    print ('o desconto do imposto de renda foi de: ', imp_renda)
    print ('o desconto do inss foi de: ', inss)
    print ('o desconto do sindicato foi de: ', sindicato)
    print ('o salário líquido é de: ', salario_lq)
    



 
