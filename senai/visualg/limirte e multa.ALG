Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   :escreva um codigo que informe a profissão de
//acordo com codigo
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/08/2021
Var
   // Seção de Declarações das variáveis
   Velocidade: real
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
  escreval ("seu limite é 50")
   escreva ("digite a sua velocidade:")
   leia (velocidade)

   se (velocidade <50) entao
      escreva ("voce ficou abaixo do limite de velocidade,  PARABÉNS")
   senao

      se (velocidade = 50) entao
         escreva ("voce ficou no limite de velocidade")
      senao

         se (velocidade >50) e (velocidade <60) entao
            escreva ("voce ultrapassou o limite, sua multa será de 50.00$")
         senao

            se (velocidade >=61) e (velocidade <81) entao
               escreva ("voce ultrapassou o limite, sua multa será de 100.00$")
            senao

               se (velocidade >=81) entao
                  escreva ("voce ultrapassou o limite, sua multa será de 200.00$")
               senao

               fimse
            fimse
         fimse
      fimse
   fimse


Fimalgoritmo