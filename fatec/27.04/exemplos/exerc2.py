def serie1():
    s = 0
    c = 1
    while c <= 10:
        s = s + 1/c
        c = c +1
    return s

def serie2(N):
    s = 0
    c = 1
    while c <= N:
        s = s + 1/c
        c = c +1
    return s

def tabuada(N):
    c = 1
    while c <= 10:
        x = N * c
        print(N, "*",  c, "=", x)
        c = c + 1

def main():
    print("série 1 = ", serie1())
    print("série 2 = ", serie2(5))
    valor = int(input("Digite um número inteiro positivo: "))
    while valor <= 0:
        valor = int(input("Digite um valor inteiro positivo: "))
    print("Série 2 = ", serie2(valor))
    tabuada(valor)


main()