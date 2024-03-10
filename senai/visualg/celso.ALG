Algoritmo "semnome"

Var
   celsius, fah, v1: real


Inicio
   celsius <- -100
   fah <- -148

   escreval ("celsius   fahrenheit")
   enquanto (celsius < 101)  e (fah < 212) faca
      celsius <- celsius + 1
      fah <- fah + 1.8
      escreval (celsius,  fah)

   fimenquanto
   se (celsius = fah) entao
      v1 <- celsius
   fimse
   escreval("as temperaturas são iguais em: ", v1)




Fimalgoritmo



