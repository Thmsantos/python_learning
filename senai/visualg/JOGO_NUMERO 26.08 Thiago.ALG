Algoritmo "semnome"

Var

   num1, cont : inteiro
Inicio
   num1 <- 760
   cont <- 0
   repita
      escreval ("informe um numero <para sair -1>: ")
      leia (num1)
      se (num1 <760) entao
       limpatela
          cont <- cont + 1
         escreval ("--chutou baixo--")
      senao
         se (num1 >760) entao
          limpatela
            cont <- cont + 1
            escreval ("--chutou alto--")
         senao
            se (num1 = 760) entao
            limpatela
               cont <- cont + 1
               escreval ("--PARABÉNS!!!-- foram necessárias", cont, " tentativas.")
            fimse
         fimse
      fimse
   ate (num1 < 0 )





Fimalgoritmo
