Algoritmo "semnome"

Var

   num1, np, nn, z, cont:inteiro

Inicio
   cont <- 0
   enquanto (cont < 3)  faca
      escreval("digite um numero: ")
      leia (num1)
      cont <- cont + 1

      se ( num1 <0 ) entao
         nn <- nn + 1
      senao

         se ( num1 = 0) entao
            z <- z+1
         senao

            np <- np + 1

         fimse
      fimse

   fimenquanto
   
   escreval("----------")
   escreval("Numero negativo ",nn)
   escreval("numero neutro ",z)
   escreval("numero positivo ",np)

Fimalgoritmo