# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 07
"""Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos"""


def ex07():
    n = int(input("Insira a quantidade de turmas \n"))
    alunos1 = 0
    for i in range(1, n + 1):
        alunos = int(input("informe a quantidade de alunos em cada turma "))
        while alunos > 40:
            alunos = int(input("valor incorreto,Limite de 40 alunos por turma  "))
        alunos1 = (alunos1 + alunos)
    media = (alunos1 / n)
    print("Então o número médio de alunos por turma é ->", media)


ex07()
