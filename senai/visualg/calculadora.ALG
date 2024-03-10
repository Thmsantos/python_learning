Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : calculadora

// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 18/08/2021
Var
// Seção de Declarações das variáveis 
 num1,num2:real
operacao:caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
 escreva ("Digite um numero:")
 leia (num1)
 
 escreva ("digite o sinal da operação:")
 leia (operacao)

 escreva ("Digite o segundo numero:")
 leia (num2)


 se (operacao = "+") entao
 escreva (num1 + num2)
 senao
 
  se (operacao = "-") entao
 escreva (num1 - num2)
  senao
 
  se (operacao = "*") entao
 escreva (num1 * num2)
  senao
  
  se (num2=0) entao
  escreva ("não é possível dividir esse número, digite um numero valido")
  senao
  
  se (operacao = "/") entao
 escreva (num1 * num2)
  senao

 fimse
 fimse
 fimse
 fimse
 fimse

 

Fimalgoritmo