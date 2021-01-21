# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 11
"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eless"""

def ex11():
    num1 = int(input("Insira um número: "))
    num2 = int(input("Insira outro número: "))

    # gere os números inteiros que estão no intervalo compreendido por eles
    for i in range(num1 + 1, num2):
        print(i, end=' ')
    for i in range(num2 + 1, num1):
        print(i, end=' ')

ex11()
