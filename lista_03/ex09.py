# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercício
"""Faça um programa que leia 5 números e informe a soma e a média dos números"""

def ex09():
    num1 = float(input("Insira o primeiro numero "))
    num2 = float(input("Insira o segundo numero "))
    num3 = float(input("Insira o terceiro numero "))
    num4 = float(input("Insira o quarto numero "))
    num5 = float(input("Insira o quinto numero : "))

    resultado= num1 + num2 + num3 + num4 + num5
    media = resultado / 5
    print("O resultado da soma é -> %d, e a media é -> %d" %(resultado, media))

ex09()
