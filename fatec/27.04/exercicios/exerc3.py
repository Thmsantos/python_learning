array = []
impares_posicao = []
impares = []

x = 1

while x != 0:
    numero = int(input('numero: '))
    array.append(numero)
    
    resto = numero%2
    
    if resto > 0:
        impares.append(numero)
        posicao = array.index(numero)
        impares_posicao.append(posicao)
    
    x = int(input('deseja continuar? 1 (sim), 0 (não): '))

soma = 0
   
for z in impares:
    soma = soma + z

print('numeros: ',impares)
print('posição: ', impares_posicao)
print(soma)