# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 01
"""Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1."""


def ex01():
    #entrada de numero
    n=int(input("Insira um numero para começar "))
    contaresto=0
    for i in range(1,n+1):
        resto=n%i
        if resto==0:
            contaresto=contaresto+1
    if contaresto==1 or contaresto==2:
        print(n,"-> é um numero primo")
    else:
        print(n,"->nao é um numero primo")

ex01()
