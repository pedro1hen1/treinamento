#Exercicio 02
#Irei organizar tudo em uma função
def CompStrings():
    #Faça um programa que leia 2 strings
    entrada1=input("Digite a primeira string ")
    entrada2=input("Digite a segunda string ")
    # informe o conteúdo delas seguido do seu comprimento.
    compri1=(len(entrada1))
    compri2=(len(entrada2))
    print("O conteúdo da primeira String é -> %s e seu comprimento é -> %d" % (entrada1, compri1))
    print("O conteúdo da segunda String é -> %s e seu comprimento é  -> %d" % (entrada2, compri2))
    #Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
    if (compri1 != compri2):
        print("O Tamanho das Strings são diferentes")
    else:
        print("O Tamanho das Strings são iguais")
    #verificar se o conteudo e igual
    if(entrada1 == entrada2):
        print("O conteudo das Strings são iguais!")
    else:
        print("O conteudo das Strings são diferentes!")   
    
CompStrings()
    
    

