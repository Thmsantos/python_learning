Algoritmo "zz"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Thiago Messias Santos
// Data atual  : 04/08/2021
Var
// Seção de Declarações das variáveis 
salario:real
novo_salario:real
acrescimo:real
  
 inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

 escreval ("informe o seu salario:")
 
         leia (salario)
         
 novo_salario <- (salario * (25/100) + salario)
 
 escreval ("valor do salario reajustado : ",novo_salario)
 
 escreval ("aumento do salario :",novo_salario - salario)
 
Fimalgoritmo