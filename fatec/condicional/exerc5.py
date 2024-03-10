num1 = float(input("numero um: "))
num2 = float(input("numero dois: "))

if num1 == num2:
    print("sao iguais")
else:
    if num1 > num2:
        print("%2.1f é maior que %2.1f" % (num1, num2))
    else:
        print("%2.1f é maior que %2.1f" % (num2, num1))