notas = [0.0] * 5
soma = 0.0
i = 0

while i < len(notas):
    notas[i] = float(input("nota %d :" %(i+1)))
    soma = soma + notas[i]
    i = i+1
    
media = soma/len(notas)

print(media)