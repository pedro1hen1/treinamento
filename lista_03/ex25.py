# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

# Exercicio 25

"""Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas."""


def ex25():
    altalunos = []
    alunos = []

    for i in range(10):
        n_aluno = int(input("Insira o número do aluno "))
        while n_aluno in alunos:
            print("Erro [Este número ja foi digitado]")
            n_aluno = int(input("Insira outro número "))
        a_aluno = altalunos.append(float(input("Insira a altura do aluno ")))
        alunos.append(n_aluno)

    indice_baixo = altalunos.index(min(altalunos))
    indice_alto = altalunos.index(max(altalunos))

    print("Aluno mais baixo \nNúmero: ", alunos[indice_baixo], "\nAltura: ", min(altalunos))
    print("Aluno mais alto \nNúmero: ", alunos[indice_alto], "\nAltura: ", max(altalunos))


ex25()
