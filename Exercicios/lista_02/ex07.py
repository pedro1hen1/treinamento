#Exercicio 07

#Guarde uma string com uma frase informada pelo usuário   
frase = str(input("Digite uma frase: "))
vog = [] 
for i in range(len(frase)):
    if frase[i] in ['a', 'e', 'i', 'o', 'u']:
        vog.append(frase[i])
        
    else:
        #variavel para contar espaços
        espacos = frase.count(' ')
        print("\nExistem ", espacos, "espaços na frase.")
        print("↓↓ Quantidade de vogais ↓↓")
        print(
        "A: ", vog.count('a'),
        "\nE: ", vog.count('e'),
        "\nI: ", vog.count('i'),
        "\nO: ", vog.count('o'),
        "\nU: ", vog.count('u'))