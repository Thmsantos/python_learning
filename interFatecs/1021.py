#Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
#A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
#As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

#Entrada
#O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

#Saída
#Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

#Obs: Utilize ponto (.) para separar a parte decimal.

#Exemplo de Entrada	Exemplo de Saída
#576.73

#NOTAS:
#5 nota(s) de R$ 100.00
#1 nota(s) de R$ 50.00
#1 nota(s) de R$ 20.00
#0 nota(s) de R$ 10.00
#1 nota(s) de R$ 5.00
#0 nota(s) de R$ 2.00
#MOEDAS:
# moeda(s) de R$ 1.00
# moeda(s) de R$ 0.50
# moeda(s) de R$ 0.25
# moeda(s) de R$ 0.10
# moeda(s) de R$ 0.05
# moeda(s) de R$ 0.01

n = float(input())

print("%d nota(s) de R$ 100.00" % int(n/100))

n = n%100
print("%d nota(s) de R$ 50.00" % int(n/50))

n = n%50
print("%d nota(s) de R$ 20.00" % int(n/20))

n = n%20
print("%d nota(s) de R$ 10.00" % int(n/10))

n = n%10
print("%d nota(s) de R$ 5.00" % int(n/5))

n = n%5
print("%d nota(s) de R$ 2.00" % int(n/2))

n = n%2
print("%d moeda(s) de R$ 1.00" % int(n/1))

n = n%1
print("%d moeda(s) de R$ 0.50" % int(n/0.50))

n = n%0.50
print("%d moeda(s) de R$ 0.25" % int(n/0.25))

n = n%0.25
print("%d moeda(s) de R$ 0.10" % int(n/0.10))

n = n%0.10
print("%d moeda(s) de R$ 0.05" % int(n/0.05))

n = n%0.05
print("%d moeda(s) de R$ 0.01" % int(n/0.01))




