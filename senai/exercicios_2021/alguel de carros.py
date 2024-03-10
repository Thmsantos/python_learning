
import datetime 
from datetime import date

veiculo = int (input ('Porte do veículo? (1 para pequeno) (2 para médio) (3 para grande): '))
kms = float (input ('Quantos kms foram rodados? '))
dias = int (input ('Quantos dias alocou o carro? '))

if veiculo == 1:
    custo_dias = (dias*180)
    custo_km = (kms*3.95)
    total = custo_dias + custo_km
    print (total)
elif veiculo == 2:
    custo_dias = (dias*220)
    custo_km = (kms*3.95)
    total = custo_dias + custo_km
    print (total)
elif veiculo == 3:
    custo_dias = (dias*180)
    custo_km = (kms*3.95)
    total = custo_dias + custo_km
    print (total)
    


