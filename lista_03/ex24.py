# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 24
"""O Departamento Estadual de Meteorologia lhe contratou para desenvolver
um programa que leia um conjunto indeterminado de temperaturas, e informe ao
final a menor e a maior temperaturas informadas, bem como a média das temperaturas"""


def ex24():

    n_temp = int(input("Insira o total de temperaturas que ira calcular "))
    temperaturas = []
    n = 1
    for i in range(n_temp):
        temperatura = temperaturas.append(float(input("Insira uma temperatura -> ")))
        n += 1

    print("Maior temperatura -> ", max(temperaturas))
    print("Menor temperatura -> ", min(temperaturas))
    print("Média -> ", round(sum(temperaturas) / len(temperaturas), 2))

ex24()
