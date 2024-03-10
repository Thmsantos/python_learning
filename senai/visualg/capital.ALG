Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : calculadora

// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/08/2021
Var
   // Seção de Declarações das variáveis

   capital : caractere
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   escreval ("informe a capital :")


   leia (capital)



   escolha (maiusc (capital))

   caso "sao paulo", "belo horizonte", "vitoria", "rio de janeiro"
      escreval ("a capital ", capital," é da região sudeste")


   caso "Natal", "joao pessoa", "salvador", "fortaleza", "sao luis", "maceio", "aracaju", "recife", "teresina"
      escreval ("a capital ", capital," é da região nordeste")

   outrocaso
      escreval ("a capital digitada é de outra regiao")
   fimescolha




Fimalgoritmo