# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 26

"""Faça um programa que peça um número inteiro positivo e em seguida mostre este número invertido.
Exemplo:
  12376489  => 98467321"""


def ex26():
    numero = input("Insira um número ")
    print("Este número invertido fica -> ", numero[:: -1])


ex26()
