Algoritmo "semnome"

Var
   motorista, maior, carteira,  carteira2, multa, multas, multas2: inteiro
   multa1, multa2, multa3, multa4, total : real
   piloto: caractere
Inicio

   para motorista de 0 ate 5 passo 1 faca

      escreval ("nome do piloto:  ")
      leia (piloto)
      escreval ("informe o número da carteira: ")
      leia (carteira)
      se (carteira > 10) entao
         escreval ("ERRO!!!, o máximo é 10 ")
      senao

         escreval ("informe o número de multas (máx 4): ")
         leia (multa)

         se (multa > 4) entao
            escreval ("ERRO!!!, o máximo é 4 ")
         senao
            se ( multa = 4) entao
               escreval ("valor da multa: ")
               escreva ("multa 1: ")
               leia (multa1)
               escreva ("multa 2: ")
               leia (multa2)
               escreva ("multa 3: ")
               leia (multa3)
               escreva ("multa 4: ")
               leia (multa4)
               total <- multa1 + multa2 + multa3 + multa4
               escreval ("o total arrecadado foi de: ", total)

               multa <- 4
               carteira <- multa
            senao

               se ( multa = 3) entao
                  escreval ("valor da multa: ")
                  escreva ("multa 1: ")
                  leia (multa1)
                  escreva ("multa 2: ")
                  leia (multa2)
                  escreva ("multa 3: ")
                  leia (multa3)
                  total <- multa1 + multa2 + multa3
                  escreval ("o total arrecadado foi de: ", total)
                  multa <- 3
               senao

                  se ( multa = 2) entao
                     escreval ("valor da multa: ")
                     escreva ("multa 1: ")
                     leia (multa1)
                     escreva ("multa 2: ")
                     leia (multa2)
                     total <- multa1 + multa2
                     escreval ("o total arrecadado foi de: ", total)
                     multa <- 2
                  senao

                     se (multa = 1) entao
                        escreval ("valor da multa: ")
                        escreva ("multa 1: ")
                        leia (multa1)
                        total <- multa1
                        escreval ("o total arrecadado foi de: ", total)
                        multas <- 1
                        motorista <- motorista + 1



                     fimse
                  fimse
               fimse
            fimse
         fimse
      fimse


      escreval ("o numero de multas de ", piloto, " foi de:", multa)
      escreval ("*************************************************")
   fimpara
   escreval ("o piloto da carteira ", carteira2 , " recebeu mais multas!! ")
   escreval ("*************************************************")
Fimalgoritmo