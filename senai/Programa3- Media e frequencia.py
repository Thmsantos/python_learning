
#entrada e calculo da media e percentual
n1 = float (input('Informe a primeira nota: '))
n2 =  float (input ('Informe a segunda nota: '))
media =  (n1 + n2) /2
print (media)
faltas= int (input ('informe a quantidade de faltas nas 100 aulas: '))
frequencia_negativa = (faltas - 100) 
frequencia = (frequencia_negativa * -1)


if media >= 7 and frequencia >75:
    print ('APROVADO')
    print ('Sua média foi de: ', media)

    print ('Sua frequencia foi de: ', frequencia,'%')
elif media <5 and frequencia <75:
    print ('REPROVADO')
    print ('Sua média foi de: ', media)
    print ('Sua frequencia foi de: ', frequencia,'%')
elif media >=5 or media <7 and frequencia >50 or frequencia <75:
    print ('RECUPERAÇÃO')
    print ('Sua média foi de: ', media)
    print ('Sua frequencia foi de: ', frequencia,'%')
