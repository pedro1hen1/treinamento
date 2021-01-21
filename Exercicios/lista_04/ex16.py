# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 16
"""Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o
"""


def ex16():
    entry_inicial = 1000
    aumento = 1.5

    for i in range(1996, 2018 + 1):
        aumento = aumento * 2
        atual = entry_inicial + (entry_inicial * (aumento / 100))
        print("Salario em ", i, " = %.02f" % atual)


ex16()
