n1 = float(input("Primeiro Numero: "))
n2 = float(input("Segundo Numero: "))

if n2 == 0:
    print('numero inválido')
else:
    print("%2.2f / %2.2f" % (n1, n2))