# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 27

"""Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
 Imprima no final a soma da série."""


def ex27():
    num1 = 1
    num2 = 1
    n1_lista = []
    n2_lista = []
    # executando como no exemplo
    print("S = ", end="")
    while num1 <= 10 - 1:
        print(num1, "/", num2, " + ", end="")
        n1_lista.append(num1)
        n2_lista.append(num2)
        num1 += 1
        num2 += 2

    print(num1, "/", num2, " = ", sum(n1_lista), "/", sum(n2_lista))


ex27()
