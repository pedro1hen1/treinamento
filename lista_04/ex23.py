# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# exercicio 23
"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
média, conforme a descrição acima informada (retirar o melhor e o pior salto e
depois calcular a média com as notas restantes). As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
"""


def ex23():
    nome_atleta = True
    n_atleta = 1
    while nome_atleta != '':
        saltos = []
        print("\n" * 5)
        print("Atleta n°", n_atleta)
        nome_atleta = input("Digite o nome do atleta: ")
        if nome_atleta == '':
            break
        else:
            n_salto = 1
            print("\n" * 3)
            for i in range(5):
                print("Salto n° ", n_salto)
                distancia_salto = float(input("Digite a distancia do salto: "))
                saltos.append(distancia_salto)
                n_salto += 1
            print("Atleta: ", nome_atleta)
            n_salto = 1
            count = 0
            for i in range(5):
                print(n_salto, "° salto : ", saltos[count], " m")
                n_salto += 1
                count += 1
            print("Melhor salto: ", max(saltos), " m")
            print("Pior salto: ", min(saltos), " m")

            saltos.remove(max(saltos))
            saltos.remove(min(saltos))
            media = sum(saltos) / len(saltos)
            print("Media dos demais saltos: ", round(media, 2))
            print("Resultado Final: \n", nome_atleta, " : ", round(media, 2))
            n_atleta += 1


ex23()
