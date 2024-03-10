Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 05/08/2021
Var
// Seção de Declarações das variáveis 
nome:caractere
distancia:real
temp:real
velocidade_media:real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreva ("nome do motorista:")
leia (nome)
escreva ("digite a distancia:")
leia (distancia)
escreva ("digite o temp:")
leia (temp)

velocidade_media <- distancia/temp

escreval ("a velocidade media do " ,  nome ,  " foi de =" , velocidade_media)


Fimalgoritmo