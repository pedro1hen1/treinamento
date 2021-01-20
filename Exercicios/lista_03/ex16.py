# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
#Exercicio 16

def ex16():
    """A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
    Faça um programa capaz de gerar a série até o n−ésimo termo.
    """
    # Começo da sequencia
    ultimo = 1
    penultimo = 1
    count = 3
    t = int(input("Insira ate qual termo deseja buscar"))
    print(ultimo)
    print(penultimo)
    while count <= 9:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print("->", termo)
ex16()
