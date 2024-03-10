Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   :escreva um codigo que informe a profissão de
//acordo com codigo
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/08/2021
Var
   // Seção de Declarações das variáveis
   salario_fixo, vendas, comissao: real
   nome:caractere
Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   escreva ("digite seu nome:")
   leia (nome)
   
   escreva ("informe seu salario fixo:")
   leia (salario_fixo)
   
   escreva ("informe o numero de vendas no mes:")
   leia (vendas)
    

    escreval ("seu salario com comissão é",  (salario_fixo+vendas*1.15))
    
    comissao <- salario_fixo*0,15

    escreval ("sua comissão é", (vendas*1.15))

   



Fimalgoritmo