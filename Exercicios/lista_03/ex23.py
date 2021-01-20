# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

import math

# Exercicio 23
"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
def ex23():
    num = int(input("\nInsira um numero para iniciar -> "))
    count = num
    fat = math.factorial(num)

    for i in range(num - 1):
        print(count, end=" * ")
        count -= 1
    print("1 = ", fat)


ex23()
