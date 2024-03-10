Algoritmo "semnome"

Var
   numero : inteiro

procedimento Tabuada (valor: inteiro)

var

   i : inteiro
inicio
   escreval ("Tabuada de ", valor, "'")
   para i de 1 ate 10 faca
      escreval (valor, " *", i, " = ", valor*i)
   fimpara
fimprocedimento

Inicio
   escreva ("Digite o número: ")
   leia (numero)
   Tabuada (numero)

Fimalgoritmo