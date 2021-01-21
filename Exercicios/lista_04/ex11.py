# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'
# Exercicio 11
"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99
e agora possui uma loja de conveniências. Faça um programa que implemente uma
caixa registradora rudimentar. O programa deverá receber um número desconhecido
de valores referentes aos preços das mercadorias. Um valor zero deve ser
informado pelo operador para indicar o final da compra. O programa deve
então mostrar o total da compra e perguntar o valor em dinheiro que o cliente
forneceu, para então calcular e mostrar o valor do troco. Após esta operação,
o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00

"""


def ex11():
    inicio = True
    while inicio > 0:
        p_prod = True
        valor_prod = []
        prod = 1

        while p_prod != 0:
            print("Lojas Tabajara")
            print("Produto", prod, ":")
            p_prod = float(input("Digite o preço do produto: "))
            valor_prod.append(p_prod)
            prod += 1

        print("Total: ", sum(valor_prod))
        dinheiro = float(input("Insira o valor que ira pagar  "))

        while dinheiro < sum(valor_prod):
            dinheiro = float(input("Insira o valor que ira pagar[maior que o total da compra] : "))

        print("Dinheiro: R$", dinheiro)
        troco = (dinheiro - sum(valor_prod))
        print("Troco: R$", troco)
        print("_" * 30)
        print("\n" * 5)
        print("Registar nova compra")
        print("_" * 30)

ex11()
