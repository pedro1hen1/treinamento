# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 16

def ex17():
    """A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
    Faça um programa que gere a série até que o valor seja maior que 500.
    """
    #Feito com base no ultimo
    # Começo da sequencia
    ultimo = 1
    penultimo = 1
    print(ultimo)
    print(penultimo)
    termo = 0
    while termo < 500:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        if termo < 500:
            print(termo)
        else:
            print("Encerrado proximo numero maior que 500")
ex17()
