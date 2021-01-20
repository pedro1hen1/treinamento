# Exercicio 13
def calcpeso():
    h = float(input("Entre com sua altura: "))
    #Peso ideal para homens: (72.7*h) - 58
    pesoh = (72.7 * h) - 58
    print("Peso ideal para Homens {:.1f}".format(pesoh))
    #Para mulheres: (62.1*h) - 44.7
    pesom = (62.1 * h) - 44.7
    print("Peso ideal para Mulheres {:.1f}".format(pesom))
    
calcpeso()
