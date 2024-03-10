Algoritmo "semnome"

Var
pcrtb, pcrtru, pcrtre, pcrtp, pcrto, pcrtbr: real
idade, idadeb, idadep : inteiro
idaderu, idadere, idadeo, especo, especb: inteiro
especre, especru, especp, espec: inteiro
opn, bom, pessimo, ruim, regular, otimo: caractere

Inicio
espec <- 0
especb <- 0
especre <- 0
especru <- 0
especp <- 0
idadeb <- 0
idadep <- 0
idaderu <- 0
idadere <- 0
idadeo <- 0



enquanto (espec < 5) faca
    espec <- espec + 1
escreval ("----------------------------------------------------------")
escreva (" Sua idade: ")
leia (idade)
escreval (" Opinião sobre o filme?  ótimo, bom, regular, ruim ou péssimo.")
leia (opn)

se (opn = otimo) entao
idadeo <- idadeo +1
especo <- especo + 1
espec <- espec + 1
senao

se (opn = bom) entao
idadeb <- idadeb + 1
especb <- especb + 1
espec <- espec + 1
senao

se (opn = regular) entao
idadere <- idadere + 1
especre <- especre + 1
espec <- espec + 1
senao

se (opn = ruim) entao
idaderu <- idaderu + 1
especru <- especru + 1
espec <- espec + 1
senao

se (opn = pessimo) entao
idadep <- idadep + 1
especp <- especp + 1
espec <- espec + 1

fimse
fimse
fimse
fimse
fimse
fimenquanto

escreval (" a quantidade de votos para ótimo foi de: ", especo)

pcrtb <- especo/espec * 100
escreva (pcrtb)
Fimalgoritmo