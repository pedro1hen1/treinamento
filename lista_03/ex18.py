# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 18
"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120"""


def ex18():
    num = int(input("Insira um numero para começar ->"))
    multiplicador = num
    while multiplicador > 1:
        multiplicador = multiplicador - 1
        num = num * multiplicador
        print(num, end='->')


ex18()
