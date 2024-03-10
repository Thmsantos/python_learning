def ParOuImpar(N):
    x = N%2
    if x == 0:
        print('par')
    elif x != 0:
        print('impar')
        
def main():
    valor = int(input("Digite um número inteiro positivo: "))
    ParOuImpar(valor)
    
main()