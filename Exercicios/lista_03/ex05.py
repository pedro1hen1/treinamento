# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 05
"""Copie o programa anterior e altere permitindo ao usuário
informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação."""


def ex05():
    # população1
    print("_" * 50)
    pop1 = float(input("Insira a população da população 1 "))
    print("_" * 50)
    # população2
    pop2 = float(input("Insira a população da população 2 "))
    print("_" * 50)
    ano = 0
    # taxa de crescimento
    cres1 = float(input("Insira taxa de crescimento da população 1 "))
    print("_" * 50)
    cres2 = float(input("Insira a taxa de crescimento da população 1 "))
    print("_" * 50)
    while pop1 < pop2:
        pop1 += round((pop1 * cres1) / 100)
        pop2 += round((pop2 * cres2) / 100)
        ano = ano + 1

    print("Em ->", ano, "anos a população 1 vai ser maior que a população 2 ")
    print("população1|", pop1, "habitantes")
    print("população2|", pop2, "habitantes")
    print("_" * 50)


ex05()
