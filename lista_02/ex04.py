#Exercicio 04
#Modifique o programa anterior de forma a mostrar o nome em formato de escada

#Faça um programa que solicite o nome do usuário
entrada = input("Insira seu nome ")
nome = entrada.upper()
#modificado laço de repetição para imprimir na vertical alterado
for i in range(0, len(nome)+1):
    print(nome[:i])