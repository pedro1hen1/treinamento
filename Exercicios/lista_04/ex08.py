# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 08
"""Faça um programa que calcule o valor total investido por um colecionador
em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um."""


def ex08():
    entry_cd = int(input("Insira o total de CDs adquiridos \n "))
    count = 0
    for i in range(1, entry_cd + 1):
        preco = float(input("Insira o preço pago por cada CD "))
        count = (count + preco)
        media = (count / entry_cd)
    print("-total investido =", count, "$")
    print("-valor gasto em cada CD =", media, "$")


ex08()
