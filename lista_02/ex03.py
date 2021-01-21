#Exercicio 03

#Faça um programa que solicite o nome do usuário
entrada = input("Insira seu nome ")
nome = entrada.upper()
#laço de repetição para imprimir na vertical
for i in range(len(nome)):
    print(nome[i])