# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 17
"""Em relação ao programa anterior, copie e altere para permitir que o usuário
digite o salário inicial do funcionário.
"""


def ex17():
    entry_inicial = float(input("Insira o valor do salario inicial do funcionário "))
    aumento = 1.5

    for i in range(1996, 2018 + 1):
        aumento = aumento * 2
        atual = entry_inicial + (entry_inicial * (aumento / 100))
        print("Salario em ", i, " = %.02f" % atual)


ex17()
