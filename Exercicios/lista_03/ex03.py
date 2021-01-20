# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 03
"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""


def ex03():
    # Nome: maior que 3 caracteres
    entry_name = input("Insira seu nome ")
    while len(entry_name) <= 3:
        entry_name = input("Digite seu nome novamente -> OBS:MAIOR QUE 3 CARACTERES ")
    else:
        print("Nome ok")

    # Idade: entre 0 e 150;
    entry_idade = int(input("Insira sua idade: "))
    while entry_idade < 0 or entry_idade > 150:
        entry_idade = int(input("Digite sua idade novamente -> OBS:entre 0 e 150 "))
    else:
        print("Idade ok")

    # Salário: maior que zero;
    entry_sal = float(input("Insira seu salario "))
    while entry_sal <= 0:
        entry_sal = float(input("Digite seu salario novamente -> salario deve ser maior que 0 "))
    else:
        print("Salario ok")
    # Sexo: 'f' ou 'm';
    entry_sexo = input("Insira o seu sexo F OU M ")
    while entry_sexo != 'f' and entry_sexo != 'm':
        entry_sexo = input("Digite o seu sexo novamente -> F OU M ")
    else:
        print("Sexo ok")
    # Estado Civil: 's', 'c', 'v', 'd';
    entry_civil = input("Insira o seu estado cívil s, c, v, d ")
    while entry_civil != 's' and entry_civil != 'c' and entry_civil != 'v' and entry_civil != 'd':
        entry_civil = input("Digite seu estado civil novamente -> s, c, v, d: ")
    else:
        print("Estado civil ok")


ex03()
