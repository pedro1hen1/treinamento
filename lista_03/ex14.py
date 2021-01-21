# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 14
"""Faça um programa que peça dois números, base e expoente,
 calcule e mostre o primeiro número elevado ao segundo número.
  Não utilize a função de potência da linguagem"""

def ex14():
    #peça dois números
    b = int(input("Insira base  "))
    e = int(input("Agora insira o expoente "))
    resultado = 1

    for i in range(e):
        #calcule e mostre o primeiro número elevado ao segundo número
        resultado = b * b
        i += 1

    print("O primeiro numero -> %d\nElevado ao segundo -> %d\nFica --> %d" % (b, e, resultado))
ex14()
