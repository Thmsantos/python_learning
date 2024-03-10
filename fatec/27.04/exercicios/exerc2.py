array = []
pares = []

x = 10

while x > 0:
    numero = int(input('numero: '))
    array.append(numero)
    
    resto = numero%2
    
    if(resto == 0):
        posicao = array.index(numero)
        pares.append(posicao)
    
    x = x - 1

print(array)
print(pares)

    