n = 0
s = 0

while  True:
    n = int (input ('digite um número (para somar os numeros acima 999) : '))
    if n == 999:
        break
    s += n

print (f'a soma vale a {s} ')
