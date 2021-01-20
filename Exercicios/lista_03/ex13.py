# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'

#Exercicio 13
'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''

def ex13():
    print("_" * 30)
    num = int(input("Insira a tabuada de 1 a 10 "))
    cont = 1

    while cont <= 10:
        result = num * cont
        print("_" * 11)
        print(num, "X", cont, "=", result)
        cont = cont + 1

ex13()

