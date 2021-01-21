# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 08
"""Faça um programa que leia 5 números e informe o maior número"""


def ex08():
    num1 = float(input("Insira o primeiro numero "))
    num2 = float(input("Insira o segundo numero "))
    num3 = float(input("Insira o terceiro numero "))
    num4 = float(input("Insira o quarto numero "))
    num5 = float(input("Insira o quinto numero : "))

    lista = [num1, num2, num3, num4, num5]

    print("_" * 40)
    print("O maior entre os 5 numero e -> ", max(lista))
    print("_" * 40)


ex08()
