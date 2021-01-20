# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 19

"""Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.
"""
def ex19():
    lista = []
    count = 0

    quant = int(input("Insira a quantidade de numeros na lista: "))
    print("OK")
    while quant != count:
        numero = lista.append(float(input("Insira um número: ")))
        count += 1
    print("_" * 30)
    print("Lista: ", lista)
    print("_" * 30)
    print("Maior| ", max(lista))
    print("Menor: ", min(lista))
    print("Soma dos resultados| ", max(lista) + min(lista))


ex19()
