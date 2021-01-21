# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 02
"""Copie e altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível."""

def ex02():
    print("_" * 40)
    num = int(input("Insira um numero para começar "))
    contaresto = 0
    lista = []

    for i in range(num):
        if num % (i + 1) == 0:
            contaresto += 1
            lista.append(i + 1)
        else:
            contaresto

    if contaresto == 1 or contaresto == 2:
        print("_" * 40)
        print("O numero e primo sendo divido por -> ", lista)

    else:
        print("_" * 40)
        print("O numero não é primo sendo divisível por -> ", lista)


ex02()
