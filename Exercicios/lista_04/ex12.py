# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 12
"""Os números primos possuem várias aplicações dentro da Computação,
por exemplo na Criptografia. Um número primo é aquele que é divisível
apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
determine se ele é ou não um número primo.
"""


def ex12():
    n = int(input("Insira um numero para começar "))
    contaresto = 0
    for i in range(1, n + 1):
        resto = n % i
        if resto == 0:
            contaresto = contaresto + 1
    if contaresto == 1 or contaresto == 2:
        print(n, "-> é um numero primo")
    else:
        print(n, "->nao é um numero primo")


ex12()
