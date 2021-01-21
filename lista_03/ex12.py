# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 12
"""Copie e altere o programa anterior para mostrar no final a soma dos números."""


def ex12():
    num1 = int(input("Insira um número: "))
    num2 = int(input("Isira um outro número: "))
    soma = 0
    while (num1 < num2 - 1):
        num1 = num1 + 1
        print(num1, end=' ')
        soma = num1 + soma

    print("\nA soma dos numeros entre o intervalo é ->", soma)

ex12()
