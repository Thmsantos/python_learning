Algoritmo "semnome"

Var
   numa : vetor [1..5] de inteiro
   numb : vetor [1..5] de inteiro
   ia, ib : inteiro
   numc, c: inteiro
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   para ia de 1 ate 5 faca
      escreva ("informe o múmero para o vetor 1 [", ia , ",1]: ")
      leia (numa[ia])
   fimpara
   limpatela
   para ib de 1 ate 5 faca
      escreva ("informe o múmero para o vetor 2 [", ib , ",1]: ")
      leia (numb[ib])
   fimpara
   limpatela
   para c de 1 ate 5 faca
      numc <- (numa[ia]+numb[ib])
      escreval ("A soma dos vetores é de: ", numc)
   fimpara
Fimalgoritmo
