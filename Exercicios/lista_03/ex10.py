# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 10
"""Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50."""
def ex10():
    #reproduz de 1 a 51 pulando duas de dois
    for impares in range(1, 51, 2):
        print(impares, end=' ')

    print("\nfinalizado")

ex10()
