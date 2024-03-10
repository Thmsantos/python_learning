Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 05/08/2021
Var
   // Seção de Declarações das variáveis

   nota1, nota2, nota3,media:real


Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreval ("informe a primeira nota:")
   leia (nota1)
   escreval ("informe a segunda nota:")
   leia (nota2)
   escreval ("informe a terceia nota:")
   leia (nota3)

   media <- (nota1+nota2+nota3)/3

   se (media >= 5) entao
      escreval ("aprovado")
   senao
      escreval ("repovado")
   fimse

Fimalgoritmo