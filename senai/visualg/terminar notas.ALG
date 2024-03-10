Algoritmo "semnome"

Var
   // Seção de Declarações das variáveis
   qntd, senhac, senha: inteiro
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   qntd <- 0
   senhac <- 1234

   repita
      escreval ("------------------------------")
      escreval (" VOCÊ TEM 5 TENTATIVAS ")
      escreval (" informe a senha: ")
      leia (senha)
      se (senha = senhac) entao
         Escreval ("~~~~~~~~~~~~~~")
         escreva (" ACESSO PERMITIDO, foram necessárias ", qntd, " tentaivas ")
      senao
         se (senha<>senhac) entao
            escreva (" ACESSO NEGADO ")
            qntd <- qntd + 1
         fimse
      fimse
   ate (qntd = 5) ou (senha=senhac)
Fimalgoritmo