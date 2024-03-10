Algoritmo "semnome"

Var
   nome, sexo:caractere
   idade, saida: inteiro
Inicio
   saida<- 1
   enquanto   (saida <>0)    faca
      escreva ("Informe seu nome:  ")
      leia (nome)

      escreva ("Informe seu sexo [M/F]: ")
      leia (sexo)

      escreva ("Informe sua idade: ")
      leia (idade)

      se (idade >=18) e (idade <=24) e (sexo = "M") entao
         escreval ("voce está apto para o exercito ")
      senao
         escreval ("voce não esta apto para o exercito")

      fimse

      escreval("-------------------")
      escreva("Quer contiunar? [0]para sair:  ")
      leia(saida)


      fimenquanto



Fimalgoritmo