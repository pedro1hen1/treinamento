# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 20
"""Copie e altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
def ex20():
    lista = []
    count = 0
    quant = int(input("Insira a quantidade de numeros na lista: "))
    print("OK")
    while quant != count:
        numero = float(input("Insira um número:: "))

        while numero > 1000 or numero < 0:
            numero = float(input("Insira um número:[erro-apenas numeros de 0 a 1000]: "))

        lista.append(numero)
        count += 1

    print("_" * 30)
    print("Lista: ", lista)
    print("_" * 30)
    print("Maior| ", max(lista))
    print("Menor: ", min(lista))
    print("Soma dos resultados| ", max(lista) + min(lista))


ex20()
