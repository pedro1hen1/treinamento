# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 13
"""Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""


def ex13():
    n = int(input("\nInsira o numero que será o final da sequencia "))
    lista_primos = []

    for i in range(n + 1):
        if i % 2 == 1 and i != 2:
            lista_primos.append(i)

    print("A sequencia de números primos -> ", lista_primos)


ex13()
