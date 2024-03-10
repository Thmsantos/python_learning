n = int(input("numero: "))

if n > 1:
    resto = n % 2
    k = 0

    if resto == 0:
        k = 0
    else:
        k = k + 1
        
    for x in range(k, n, +2):
        print(x)
        
elif n == 0:
    print('os valores são iguais')
    
else:
    resto = n % 2
    k = 0

    if resto == 0:
        k = 0
    else:
        k = k + 1
        

    for x in range(k, n, -2):
        print(x)
            

