# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 21

"""Copie e altere o programa de cálculo do fatorial, permitindo ao usuário
alcular o fatorial várias vezes e limitando o fatorial a números inteiros
positivos e menores que 16."""


def ex21():
    while 1 == 1:
        num = int(input("informe um numero-->"))
        while num > 16 or num < 0:
            num = int(input("numero incorreto,informe outro numero-->"))
        else:
            multiplicador = num
        while multiplicador > 1:
            multiplicador = multiplicador - 1
            num = num * multiplicador
            print(num, end='-> ')

ex21()
