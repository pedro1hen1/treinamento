# Exercicio 9

def convertFtoC():
    fht = float(input("Insira temperatura em fahrenheit "))
#C = 5 * ((F-32) / 9). segue a baixo a formula de calculo
    cel = 5 *((fht - 32) / 9)
    print(fht, 'graus em fahrenheit são {:.2f}'.format(cel), "Em graus celsius")

convertFtoC()