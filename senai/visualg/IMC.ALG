Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   :escreva um codigo que informe a profissão de
//acordo com codigo
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/08/2021
Var
   // Seção de Declarações das variáveis
   altura, peso, imc: real
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   escreval ("digite a sua altura:")
   leia (altura)

   escreval ("digite o seu peso:")
   leia (peso)

   escreval ("________________________________________")

  imc <- (peso / altura^2)

   se (imc <18) entao
      escreval ("magreza")
   senao

      se (imc >=18) e (imc <24.9) entao
         escreval ("saudavel, seu IMC é: ", imc)
      senao

         se (imc >=25) e (imc <29.9) entao
            escreval ("sobrepeso")
         senao

            se (imc >=30) entao
               escreval ("obesidade")
            senao

            fimse
         fimse
      fimse
   fimse




Fimalgoritmo