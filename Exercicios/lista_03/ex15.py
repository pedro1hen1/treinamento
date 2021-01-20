# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
#Exercicio 15
"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

def ex15():
    print("_" * 30)
    n1 = int(input("\nInsira o 1º número: "))
    print("_" * 30)
    n2 = int(input("Insira o 2º número: "))
    print("_" * 30)
    n3 = int(input("Insira o 3ºnúmero: "))
    print("_" * 30)
    n4 = int(input("Insira o 4º número: "))
    print("_" * 30)
    n5 = int(input("Insira o 5º número: "))
    print("_" * 30)
    n6 = int(input("Insira o 6º número: "))
    print("_" * 30)
    n7 = int(input("Insira o 7º número: "))
    print("_" * 30)
    n8 = int(input("Insira o 8º número: "))
    print("_" * 30)
    n9 = int(input("Insira o 9º número: "))
    print("_" * 30)
    n10 = int(input("Insira o 10º número: "))
    print("_" * 30)
    lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

    par = 0
    impar = 0

    for value in lista:
        if value % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

    print("Par-> ", par, "\nImpar-> ", impar)

ex15()















