# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 03
"""Faça um programa que mostre todos os primos entre 1 e N sendo N um número
inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
divisões que ele executou para encontrar os números primos. Serão avaliados o
funcionamento, o estilo e o número de testes (divisões) executados."""


def ex03():
    n = int(input("|Insira um número "))
    lista = []
    divisoes = 0

    for i in range(n + 1):
        if i % 2 == 1 and i != 2:
            lista.append(i)
            divisoes += 1
        else:
            divisoes += 1
    print("|Números primos ->", lista, "\n|Executou", divisoes, "divisões")


ex03()
