# Exercicio 16

def lojatintas():
    #o tamanho em metros quadrados da área a ser pintada
    tam = float(input("Insira o tamanho da parede a ser pintada "))
    #1 litro para cada 3 metros quadrados
    lt= tam/3

    #a tinta é vendida em latas de 18 litros
    quantL = 18
    #que custam R$ 80,00
    valorL = 80.0

    #calcule quantidade de latas de tinta a serem compradas e o preço total
    latas = (lt / quantL)
    total = (latas * valorL)

    print("É nescessario {:.2f}".format(latas),"latas de tinta")
    print("Em um valor total de R$ {:.2f}".format(total))

    
    
lojatintas()
