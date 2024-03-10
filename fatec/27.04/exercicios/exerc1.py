numeros = []

x = 10

while x > 0:
    numero = float(input('numero: '))
    numeros.append(numero)
    x = x - 1
    
numeros.reverse()
print(numeros)