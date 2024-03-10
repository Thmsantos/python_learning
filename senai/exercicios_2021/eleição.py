n = 0

while  True:

    n = int (input ('deseja continuar? (1 sim) (0 não) : '))

    if n == 0:
            break
    else:
        print ('!!ELEIÇÕES!!')
        cand = int (input ('Deseja votar em qual candidato? (1 Azulão) ¨ (2 JK) ¨ (3 Vargas) ¨ (4 branco) ¨ (5 nulo)'))
    
while ( cand < 6 ):
    
    if (cand == 1):
        azulao = 0
        azulao = azulao + 1
    elif (cand == 2):
         jk = 0
         jk = jk + 1
    elif (cand == 3):
          vargas = 0
          vargas = vargas + 1
    elif (cand == 4):
          branco = 0
          branco = branco + 1
    elif (cand == 5):
          nulo = 0
          nulo = nulo + 1
    else:
          print ('SEGUE O RESULTADO!!')
          percentualn = (nulo / 5 ) * 100
          percentualb = (branco / 5) * 100
          print ('Azulão: ',azulao)
          print ('JK: ',jk)
          print ('Vargas: ',vargas)
          print ('branco: ',branco)
          print ('nulo: ',nulo)
          print('---------')
          print ('a porcentagem de nulos e brancos respectivamente, foi de: ',nulo ,'e' ,branco)

