# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
#exercicio 18
"""Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).


Deseja-se saber:
Qual o maior e menor índice de acidentes de trânsito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
def ex18():
    codigo = int(input("Insira o código da cidade-> "))
    veiculos = int(input("Insira o número de veículos -> "))
    acidente = int(input("Insira o número de acidentes de transito com vitimas-> "))
    contaveiculos=veiculos
    maior_acidente=acidente
    menor_acidente=acidente
    contador=0
    for i in range(0,4):
        if veiculos>2000:
            contador=contador+1
            acidente_veiculos=acidente
            acidente_veiculos=acidente+acidente_veiculos
        codigo = int(input("Informe o código da cidade-> "))
        veiculos = int(input("Informe o número de veículos de passeio-> "))
        acidente = int(input("Informe o número de acidentes de transito com vitimas-> "))
        contaveiculos=contaveiculos+veiculos
        if acidente > maior_acidente:
            maior_acidente=acidente
            codigomaior=codigo
        elif acidente<menor_acidente:
            menor_acidente=acidente
            codigomenor=codigo
    media2k=(acidente_veiculos/contador)
    print("_"*80)
    print("O menor indice esta na cidade de de codigo ->", codigomenor ,"com",menor_acidente,"acidentes" )
    print("_"*80)
    print("-o maior indice  está na cidade com codigo->", codigomaior ,"com",maior_acidente,"acidentes")
    print("_"*80)
    print("Todas as cidades acumulam um total de ->", contaveiculos,"veiculos, sendo a media de ->",contaveiculos/5,"veiculos por cidade")
    print("_"*80)
    print("média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio", media2k )

