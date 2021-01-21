# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 06
"""Numa eleição existem três candidatos. Faça um programa que peça o número
total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
de votos de cada candidato"""


def ex06():
    n = int(input("Insira quantidade de eleitores "))
    votos = []
    for x in range(n):
        voto = votos.append(int(input("Insira o numero do candidato que ira votar [1, 2, 3] -> ")))

    print("candidato 1|", votos.count(1))
    print("candidato 2|", votos.count(2))
    print("candidato 3|", votos.count(3))


ex06()
