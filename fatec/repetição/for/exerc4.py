n = int(input("numero: "))

if n > 1:
    for x in range(1, n):
        print(x)
elif n == 0:
    print('os valores são iguais')
else:
    for x in range(n , 1):
        print(x)
            