#Exercicio 05
#pegando o exercicio anterior e trasnformando em escada invertida

#Faça um programa que solicite o nome do usuário
entrada = input("Insira seu nome ")
nome = entrada.upper()
#variavel que pega o tamanho da entrada
t = len(entrada)
#modificado laço de repetição para imprimir na vertical alterado
for i in range(0, len(nome)+1):
    print(nome[0:t-i])