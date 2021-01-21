# Exercicio 14

def pesopeixe():
    pesopeixe = float(input("Insira o peso do peixe "))
    #SE O PEIXE FOR MAIOR QUE O ESTAVELECIDO APLIQUE IF
    if pesopeixe > 50:
    #Gravar na variável excesso a quantidade de quilos além do limite
        excesso = (pesopeixe - 50)
    #variável multa, o valor da multa que João deverá pagar
        multa = (excesso * 4)
        print("Total de quilos além do limite " + str(excesso))
        print("Valor da multa que João deverá pagar "  + str(multa))
    
    else:
        print("Dentro do regulamento, Não teve excesso")
    
pesopeixe()

