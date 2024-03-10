Algoritmo "semnome"

Var
   n1, cont, soma:inteiro
   resul: real

Inicio
   cont <- 0
   resul <- 0
   soma <- 0

   enquanto n1 >= 0 faca
      escreval ("INFORME UM NUMERO<para sair digite -1>" )
      leia (n1)
      se (n1 >= 0)entao
         cont <- cont +1
         soma <- soma + n1
      fimse
   fimenquanto
   resul <- soma/ cont


   escreval ("a media e = ", resul)
fimalgoritmo
