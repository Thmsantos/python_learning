Algoritmo "semnome"

Var
   soma1, soma2, porcentagem : real
   alunos, alunos_acima, alunos_abaixo, alunos_p, alunos_f : inteiro  // acumuladores
   gastodes, porcentagem_a, pessoal, familiar, alim : inteiro
Inicio
   alunos <- 0
   alunos_acima <- 0
   alunos_abaixo <- 0
   alunos_p <- 0
   enquanto (alunos <>4) faca
      escreval ("-------------------------------------")

      escreval("Renda pessoal: ")
      leia (pessoal)

      escreval ("Renda familiar: ")
      leia (familiar)

      escreval ("Gasto com alimentos: ")
      leia (alim)

      escreval ("qual é o gasto com outras despesas:  ")
      leia (gastodes)

      se (gastodes < 200) entao
         alunos_abaixo <- alunos_abaixo + 1
         alunos <- alunos + 1
      senao
         se (gastodes > 200) entao
            alunos <- alunos + 1
            alunos_acima <- alunos_acima + 1


         fimse
      fimse
      se (pessoal > familiar) entao
         alunos_p <- alunos_p + 1
      fimse
      limpatela
   fimenquanto
   soma1 <- pessoal + familiar
   soma2 <- alim + gastodes
   porcentagem <- ((soma2*100) / (soma1))
   porcentagem_a <- alunos_acima * alunos (/100)
   escreval ("A porcentagem de alunos que gasta acima de 200 :" ,porcentagem_a )
   escreval ("o número de alunos com renda pessoal maior que familiar: ",  alunos_p )
   escreval ("percentual gasto relação as rendas é: ", porcentagem)
Fimalgoritmo