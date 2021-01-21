# Exercicio 10
def convertCtoF():
    cel= float(input("Insira temperatura em celcius "))
    # (celcius × 9/5) + 32 = °F. segue a baixo a formula de calculo
    fht = (cel * 9/5) + 32
    print(cel, 'graus em celsius são {:.2f}'.format(fht), "Em graus Fahrenheit")

convertCtoF()