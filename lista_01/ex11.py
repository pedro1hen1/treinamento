# Exercicio 11
def calcNums():
    num1=int(input("Insira um numero inteiro "))
    num2=int(input("Insira um outro numero inteiro "))
    real=float(input("Insira um numero real "))
    #o produto do dobro do primeiro com metade do segundo 
    result1=(num1 * 2) + (num2 / 2)
    print("Resultado do dobro do primeiro com a metade do segundo = ", result1)
    #a soma do triplo do primeiro com o terceiro
    result2=(3 * num1) + real
    print("Resultado da soma do triplo do primeiro com o terceiro ", result2)
    #o terceiro elevado ao cubo
    result3=(real ** 3)
    print("Resultado do terceiro elevado ao cubo {:.4f}".format(result3))
    

calcNums()