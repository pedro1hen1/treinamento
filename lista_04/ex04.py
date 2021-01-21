# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 04
"""Faça um programa que leia uma quantidade indeterminada de números positivos
e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75]
e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""


def ex04():

    print("_" * 80)
    print("O programa se encerra quando a entrada for lida com número negativo")
    print("_" * 80)
    lista25 = []
    lista50 = []
    lista75 = []
    lista100 = []
    n = True
    while n > 0:
        n = float(input("Insira o numero "))
        if n > 0 and n <= 25:
            lista25.append(n)
        elif n > 25 and n <= 50:
            lista50.append(n)
        elif n > 50 and n <= 75:
            lista75.append(n)
        elif n > 75 and n <= 100:
            lista100.append(n)

    print("\n[0-25]-> ", len(lista25))
    print("[26-50]-> ", len(lista50))
    print("[51-75]-> ", len(lista75))
    print("[76-100]-> ", len(lista100))


ex04()
