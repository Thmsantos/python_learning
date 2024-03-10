Algoritmo "semnome"

Var
   num1, res: real

Inicio




   repita
      escreval ("informe o numero <para sair -1>: ")
      leia (num1)
      se (num1 > 0) entao

         res <- raizq (num1)
         escreval ("a raiz de ", num1, " é ", res)
      fimse
   ate (num1 < 0)





Fimalgoritmo
