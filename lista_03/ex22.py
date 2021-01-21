# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 22
"""Faça um programa que calcule e mostre a média aritmética de N notas."""


def ex22():
    quant_notas = int(input("Digite o número de notas que você irá digitar: "))
    count = 0
    totalnotas = []

    while count < quant_notas:
        notas = totalnotas.append(float(input("\nInsira a nota -> ")))
        count += 1

    media = sum(totalnotas) / quant_notas
    print("O calculo da media e -> ", media)


ex22()
