# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 01
"""Faça um programa que peça uma nota, entre zero e dez.
 Mostre uma mensagem caso o valor seja inválido e
 continue pedindo até que o usuário informe um valor válido"""


def ex01():
    entrada = float(input("Insira uma nota de  0 a 10: "))
    while entrada < 0 or entrada > 10:
        entrada = float(input("Valor inserido incorretamente -> Digite uma nota entre 0 e 10: "))

    print("nota:", entrada)


ex01()
