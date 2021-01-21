#Exercicio 08

print("↓"*30)
def indPalidromo():
#Um programa que leia uma seqüência de caracteres
    mensagem=str(input("Insira uma frase: ")).lower()
    #declarada 'msg' que troca o espaço por espaço vazio
    msg=mensagem.replace(' ', '')
    #msg_inv inverte a mensagem para verificar se e um Palindromo
    msg_inv=msg[:: -1]
    #palavras Palindromo:osso,oco,radar
    #frases Palindromo:A gorda ama a droga,A grama é amarga
    if msg==msg_inv:
        print("A frase inserida foi ->", msg_inv)
        print("A frase ao contrario ->", msg)
        print("Logo e um Palindromo!")
    else:
        print("A frase inserida foi ->", msg_inv)
        print("A frase ao contrario ->", msg)
        print("A frase inserida não e um Palindromo")
        
indPalidromo()