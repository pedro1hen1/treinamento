#Exercicio 02

# Faça um programa que permita ao usuário digitar o seu nome
nome=input("Digite seu nome ")
#Converter as letras para maiscula
n=nome.upper()
#Em seguida mostre o nome do usuário de trás para frente
print("O nome -> %s de trás para frente fica -> %s " % (n, n[::-1]))   

