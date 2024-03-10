saida = 0
while (saida != -1):
    peso = float (input ('Peso dos peixes: '))
    if (peso <= 50):
        print ('não há excesso de peso!')
    elif (peso > 50):
        peso_adc = peso - 50
        multa = peso_adc * 40.00
        print ('a multa é de :' ,multa, ' reais!')

    saida = int( input ('deseja sair? (-1) sim - (2) não : '))



        
