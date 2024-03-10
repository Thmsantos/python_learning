Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   :Escreva um algoritmo em portigues estruturado que leia a idade de um índividuo e escreva a faixa etária a que pertence.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/08/2021
Var
// Seção de Declarações das variáveis 
idade: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
 Escreva ("Digite a idade:")
 leia (idade)
 
 se (idade >=1) e (idade <=12) entao
  escreva ("criança")
 fimse


 se (idade >=13) e (idade <=17) entao
  escreva ("adolescente")
 fimse
 
 se (idade >=18) e (idade <=59) entao
  escreva ("adulto")
 fimse
 
 se (idade >=60) entao
  escreva ("especialista")
 fimse

Fimalgoritmo