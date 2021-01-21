# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
"""Faça um programa que leia um nome de usuário
 e a sua senha e não aceite a senha igual ao nome do usuário,
  mostrando uma mensagem de erro e voltando a pedir as informações."""


# Exercicio 02
def ex02():
    print("_" * 40)
    entrada1 = input("Insira o nome de usuario ")
    print("_" * 40)
    entrada2 = input("Agora insira a senha ")

    while entrada1 == entrada2:
        print("Invalido, Insira uma senha difente do nome de usuario")
        entrada1 = input("insira o seu nome de usuario: ")
        entrada2 = input("Insira a sua senha: ")
    else:
        print("acesso permitido")


ex02()
