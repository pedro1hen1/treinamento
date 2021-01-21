# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
#Exercicio 05
"""Faça um programa que peça para n pessoas a sua idade, ao final o programa
deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada."""

def ex05():
    print("_"*50)
    n_notas=int(input("Insira a quantidade de pessoas que tem na turma-> "))
    print("_"*50)
    print("Agora insira a idade de cada uma delas->")
    print("_"*50)
    contadora=0
    for i in range(1,n_notas+1):
        notas=int(input("-informe a idade :\n"))
        contadora=contadora+notas
    media=contadora/n_notas
    print("a média de idade da turma é-->",media)
    if media<=25:
        print("Turma de jovens")
    elif media>26 and media<60:
        print("Turma de adultos")
    else:
        print("Turma de idosos")
ex05()
