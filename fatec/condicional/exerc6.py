numero = float(input("numero: "))

if numero == 0:
    print("%2.2f é igual a zero." % (numero))
if 0 > numero:
    print("%2.2f é negativo." % (numero))
else:
    print("%2.2f é positivo." % (numero))