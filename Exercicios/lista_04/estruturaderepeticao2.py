# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@pedro1hen1'



def ex01():
    #Exercicio 01
    """Faça um programa que peça um número inteiro e determine se ele é ou não 
    um número primo. Um número primo é aquele que é divisível somente por ele 
    mesmo e por 1."""
    #entrada de numero
    n=int(input("Insira um numero para começar "))
    contaresto=0
    for i in range(1,n+1):
        resto=n%i
        if resto==0:
            contaresto=contaresto+1
    if contaresto==1 or contaresto==2:
        print(n,"-> é um numero primo")
    else:
        print(n,"->nao é um numero primo")
        


def ex02():
    #Exercicio 02
    """Copie e altere o programa de cálculo dos números primos, informando, 
    caso o número não seja primo, por quais número ele é divisível.
    """
    print("_" * 40)
    num = int(input("Insira um numero para começar "))
    contaresto = 0
    lista = []

    for i in range(num):
        if num % (i + 1) == 0:
            contaresto += 1
            lista.append(i + 1)
        else:
            contaresto

    if contaresto == 1 or contaresto == 2:
        print("_" * 40)
        print("O numero e primo sendo divido por -> ", lista)

    else:
        print("_" * 40)
        print("O numero não é primo sendo divisível por -> ", lista)
        



def ex03():
    # Exercicio 03
    """Faça um programa que mostre todos os primos entre 1 e N sendo N um número
    inteiro fornecido pelo usuário. O programa deverá mostrar também o número de
    divisões que ele executou para encontrar os números primos. Serão avaliados o
    funcionamento, o estilo e o número de testes (divisões) executados."""
    n = int(input("|Insira um número "))
    lista = []
    divisoes = 0

    for i in range(n + 1):
        if i % 2 == 1 and i != 2:
            lista.append(i)
            divisoes += 1
        else:
            divisoes += 1
    print("|Números primos ->", lista, "\n|Executou", divisoes, "divisões")
    

def ex04():
    # Exercicio 04
    """Faça um programa que leia uma quantidade indeterminada de números positivos
    e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75]
    e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo."""

    print("_" * 80)
    print("O programa se encerra quando a entrada for lida com número negativo")
    print("_" * 80)
    lista25 = []
    lista50 = []
    lista75 = []
    lista100 = []
    n = True
    while n > 0:
        n = float(input("Insira o numero "))
        if n > 0 and n <= 25:
            lista25.append(n)
        elif n > 25 and n <= 50:
            lista50.append(n)
        elif n > 50 and n <= 75:
            lista75.append(n)
        elif n > 75 and n <= 100:
            lista100.append(n)

    print("\n[0-25]-> ", len(lista25))
    print("[26-50]-> ", len(lista50))
    print("[51-75]-> ", len(lista75))
    print("[76-100]-> ", len(lista100))
    


def ex05():
    #Exercicio 05
    """Faça um programa que peça para n pessoas a sua idade, ao final o programa
    deverá verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e
    maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
    média calculada."""
    print("_"*50)
    n_notas=int(input("Insira a quantidade de pessoas que tem na turma-> "))
    print("_"*50)
    print("Agora insira a idade de cada uma delas->")
    print("_"*50)
    contadora=0
    for i in range(1,n_notas+1):
        notas=int(input("-informe a idade :\n"))
        contadora=contadora+notas
    media=contadora/n_notas
    print("a média de idade da turma é-->",media)
    if media<=25:
        print("Turma de jovens")
    elif media>26 and media<60:
        print("Turma de adultos")
    else:
        print("Turma de idosos")
        



def ex06():
    # Exercicio 06
    """Numa eleição existem três candidatos. Faça um programa que peça o número
    total de eleitores. Peça para cada eleitor votar e ao final mostrar o número
    de votos de cada candidato"""
    n = int(input("Insira quantidade de eleitores "))
    votos = []
    for x in range(n):
        voto = votos.append(int(input("Insira o numero do candidato que ira votar [1, 2, 3] -> ")))

    print("candidato 1|", votos.count(1))
    print("candidato 2|", votos.count(2))
    print("candidato 3|", votos.count(3))


def ex07():
    # Exercicio 07
    """Faça um programa que calcule o número médio de alunos por turma. Para isto,
    peça a quantidade de turmas e a quantidade de alunos para cada turma.
    As turmas não podem ter mais de 40 alunos"""
    n = int(input("Insira a quantidade de turmas \n"))
    alunos1 = 0
    for i in range(1, n + 1):
        alunos = int(input("informe a quantidade de alunos em cada turma "))
        while alunos > 40:
            alunos = int(input("valor incorreto,Limite de 40 alunos por turma  "))
        alunos1 = (alunos1 + alunos)
    media = (alunos1 / n)
    print("Então o número médio de alunos por turma é ->", media)
    



def ex08():
    # Exercicio 08
    """Faça um programa que calcule o valor total investido por um colecionador
    em sua coleção de CDs e o valor médio gasto em cada um deles.
    O usuário deverá informar a quantidade de CDs e o valor para em cada um."""
    entry_cd = int(input("Insira o total de CDs adquiridos \n "))
    count = 0
    for i in range(1, entry_cd + 1):
        preco = float(input("Insira o preço pago por cada CD "))
        count = (count + preco)
        media = (count / entry_cd)
    print("-total investido =", count, "$")
    print("-valor gasto em cada CD =", media, "$")


def ex09():
    # Exercicio 09
    """O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99,
    com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente
    deve pagar ele desenvolveu um tabela que contém o número de itens que o
    cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa
    precisa apenas contar quantos itens o cliente está levando e olhar na tabela
    de preços. Você foi contratado para desenvolver o programa que monta esta
    tabela de preços, que conterá os preços de 1 até 50 produtos,
    conforme o exemplo abaixo:
    Lojas Quase Dois - Tabela de preços
    1 - R$ 1.99
    2 - R$ 3.98
    ..
    50 - R$ 99.50
    """
    for c in range(1, 51):
        count = 1.99 * c
        print(c, "-", "R$", count)
        
def ex10():
    # Exercicio 10
    """O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar
    a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.
    Você foi contratado para desenvolver o programa que monta a
    tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão
    informado pelo usuário, conforme o exemplo abaixo:
    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ..
    50 - R$ 9.00
    
    """
    pao=float(input("Insira o valor de cada pão "))
    print("Panificadora Pão de Ontem - Tabela de preços")
    for i in range(1,50+1):
        count=pao*i
        print(i,"-","R$",count)
        
def ex11():
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
        

def ex12():
    # Exercicio 12
    """Os números primos possuem várias aplicações dentro da Computação,
    por exemplo na Criptografia. Um número primo é aquele que é divisível
    apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
    determine se ele é ou não um número primo.
    """
    n = int(input("Insira um numero para começar "))
    contaresto = 0
    for i in range(1, n + 1):
        resto = n % i
        if resto == 0:
            contaresto = contaresto + 1
    if contaresto == 1 or contaresto == 2:
        print(n, "-> é um numero primo")
    else:
        print(n, "->nao é um numero primo")

def ex13():
    # Exercicio 13
    """Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
    lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
    """
    n = int(input("\nInsira o numero que será o final da sequencia "))
    lista_primos = []

    for i in range(n + 1):
        if i % 2 == 1 and i != 2:
            lista_primos.append(i)

    print("A sequencia de números primos -> ", lista_primos)
    

def ex12():
    # Exercicio 12
    """Os números primos possuem várias aplicações dentro da Computação,
    por exemplo na Criptografia. Um número primo é aquele que é divisível
    apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
    determine se ele é ou não um número primo.
    """
    n = int(input("Insira um numero para começar "))
    contaresto = 0
    for i in range(1, n + 1):
        resto = n % i
        if resto == 0:
            contaresto = contaresto + 1
    if contaresto == 1 or contaresto == 2:
        print(n, "-> é um numero primo")
    else:
        print(n, "->nao é um numero primo")
        

def ex13():
    # Exercicio 13
    """Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
    lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
    """
    n = int(input("\nInsira o numero que será o final da sequencia "))
    lista_primos = []

    for i in range(n + 1):
        if i % 2 == 1 and i != 2:
            lista_primos.append(i)

    print("A sequencia de números primos -> ", lista_primos)


def ex14():
    # Exercicio 14
    """Desenvolva um programa que faça a tabuada de um número qualquer
    inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente
    iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
    também pelo usuário, conforme exemplo abaixo:
    Montar a tabuada de: 5
    Começar por: 4
    Terminar em: 7
    
    Vou montar a tabuada de 5 começando em 4 e terminando em 7:
    5 X 4 = 20
    5 X 5 = 25
    5 X 6 = 30
    """
    print("_" * 50)
    tabuada = int(input("\nDigite o número para fazer a tabuada: "))
    inicio = int(input("Iniciar a tabuada no : "))
    fim = int(input("Finalizar a tabuada no : "))

    count = inicio

    for i in range(inicio, fim + 1):
        print(tabuada, " X ", count, " = ", tabuada * count)
        count += 1
        
def ex15():
    # exercicio 15
    """Uma academia deseja fazer um censo entre seus clientes para descobrir o
    mais alto, o mais baixo, o mais pesado e o mais leve, para isto você deve fazer
    um programa que pergunte a cada um dos clientes da academia seu código, sua a
    ltura e seu peso. O final da digitação de dados deve ser dada quando o usuário
    digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser
    informados os códigos e valores do cliente mais alto, do mais baixo, do mais
    pesado e do mais leve, além da média das alturas e dos pesos dos clientes.
    """
    cod_clientes = []
    altura_clientes = []
    peso_clientes = []
    n_cliente = 1
    codigo = True
    print("programa se encerra quando e digitado 0")
    while codigo != 0:
        print("\nCliente", n_cliente)
        codigo = int(input("Digite o código: "))
        if codigo == 0:
            break
        else:
            altura = float(input("Digite a altura: "))
            peso = float(input("Digite o peso: "))
            cod_clientes.append(codigo)
            altura_clientes.append(altura)
            peso_clientes.append(peso)
            n_cliente += 1

    cod_magro = peso_clientes.index(min(peso_clientes))
    cod_gordo = peso_clientes.index(max(peso_clientes))
    cod_alto = altura_clientes.index(max(altura_clientes))
    cod_baixo = altura_clientes.index(min(altura_clientes))
    print("\n" * 5)
    print("Código do mais magro: ", cod_clientes[cod_magro])
    print("Código do mais gordo: ", cod_clientes[cod_gordo])
    print("Código do mais alto: ", cod_clientes[cod_alto])
    print("Código do mais baixo: ", cod_clientes[cod_baixo])
    print("Média de altura: ", sum(altura_clientes) / len(altura_clientes))
    print("Média de peso: ", sum(peso_clientes) / len(peso_clientes))

def ex16():
    # Exercicio 16
    """Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
    dobro do percentual do ano anterior. Faça um programa que determine o
    """
    entry_inicial = 1000
    aumento = 1.5

    for i in range(1996, 2018 + 1):
        aumento = aumento * 2
        atual = entry_inicial + (entry_inicial * (aumento / 100))
        print("Salario em ", i, " = %.02f" % atual)
        

def ex17():
    # Exercicio 17
    """Em relação ao programa anterior, copie e altere para permitir que o usuário
    digite o salário inicial do funcionário.
    """

    entry_inicial = float(input("Insira o valor do salario inicial do funcionário "))
    aumento = 1.5

    for i in range(1996, 2018 + 1):
        aumento = aumento * 2
        atual = entry_inicial + (entry_inicial * (aumento / 100))
        print("Salario em ", i, " = %.02f" % atual)
        

def ex18():
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

def ex19():
    #Exercicio 19
    """Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
    valor dos juros, quantidade de parcelas e valor da parcela.
    Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
    1       0
    3       10
    6       15
    9       20
    12      25
    Exemplo de saída do programa:
     Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1.000,00     0               1                       R$  1.000,00
    R$ 1.100,00     100             3                       R$    366,00
    R$ 1.150,00     150             6                       R$    191,67
    """

    divida = float(input("Insira o valor da sua divida atual para consultar tabela: "))
    parcela = 1
    
    print("Valor da divida: ", end="  ")
    print("Valor do juros: ", end="  ")
    print("Quantidade de parcelas: ", end="  ")
    print("Valor da parcela: ")
    
    for i in range(5):
        if parcela == 1:
            juros = 1
            v_juros = 0
        elif parcela == 4:
            parcela = 3
            juros = 1.10
        elif parcela == 7 or parcela == 6:
            parcela = 6
            juros = 1.15
        elif parcela == 10 or parcela == 9:
            parcela = 9
            juros = 1.20
        elif parcela == 13 or parcela == 12:
            parcela = 12
            juros = 1.25
    
        v_juros = divida * (juros - 1)
        divida_com_juros = divida * juros
        valor_parcela = divida_com_juros / parcela
    
        print("R$", round(divida_com_juros, 2), end="            ")
        print(round(v_juros, 2), end="                  ")
        print(parcela, end="                        ")
        print("R$ ", round(valor_parcela, 2))
        parcela += 3


def ex20():
    # exercicio 20
    """O cardápio de uma lanchonete é o seguinte:
    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
    
    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
    Em uma eleição presidencial existem
    """
    codigos = [100, 101, 102, 103, 104, 105]
    comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'ChesseBurguer', 'Refrigerante']
    precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
    codigo = True
    n_pedido = 1
    pedido = []
    print("segue o codigo dos itens")
    print(
        "Cachorro Quente = 100- Baurus simples = 101 -Bauru com ovo = 102- Hamburguer = 103, ChesseBurguer = 104- Refrigerante = 105")
    print("_" * 120)
    while codigo != 0:
        print("\nPedido:", n_pedido)
        codigo = int(input("Digite o código do alimento: "))
        if codigo == 0:
            break
        else:
            while codigo not in codigos:
                print("codigo não existe")
                codigo = int(input("Insira o código do alimento: "))

            indice = codigos.index(codigo)
            quantidade = int(input("Insira a quantidade: "))
            valor_pedido = precos[indice] * quantidade
            pedido.append(valor_pedido)
        n_pedido += 1

    pedido_nota = 0
    print("\n" * 2)
    for i in range(n_pedido - 1):
        print("Pedido ", pedido_nota + 1, ": = R$", round(pedido[pedido_nota], 2))
        pedido_nota += 1
    print("Total: R$", round(sum(pedido), 2))
    

def ex21():
    # exercicio 21
    """Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
    1 , 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco
    
    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos.
    Para finalizar o conjunto de votos tem-se o valor zero.
    
    """
    possiveis_votos = [1, 2, 3, 4, 5, 6]
    candidatos = ['Boulos', 'Jair Bolsonaro', 'João Amoedo', 'Dilma do chefe', 'Nulo', 'Branco']
    votos = []
    print("canditado 1 = Boulos, 2 =Jair Bolsonaro,3=João Amoedo, 4=Dilma do chefe, 5=Nulo,6=Branco")
    print("contagem encerra quando digitar 0")
    voto = True
    n_votos = 1
    while voto != 0:
        print("Voto ", n_votos)
        voto = int(input("Digite o seu voto: "))
        if voto == 0:
            break
        else:
            while voto not in possiveis_votos:
                print("[Voto invalido.]")
                voto = int(input("Digite o seu voto: "))
            votos.append(voto)
        n_votos += 1

    contador = 0
    print("\n" * 2)
    for i in range(len(candidatos)):
        print("Votos para ", candidatos[contador], end=" : ")
        if votos.count == 0:
            print("0")
            contador += 1
        else:
            print(votos.count(contador + 1))
            contador += 1

    porcentagem_nulo = (votos.count(5) / len(votos)) * 100
    porcentagem_branco = (votos.count(6) / len(votos)) * 100
    print("\nPorcentagem Nulos: ", round(porcentagem_nulo, 2), "%\nPorcentagem Brancos: ", round(porcentagem_branco, 2),
          "%")
          
def ex22():
    # exercicio 22
    """Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
    o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito
    da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
    Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
    Após todos os alunos terem respondido informar:
    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
    Gabarito da Prova:
    01 - A
    02 - B
    03 - C
    04 - D
    05 - E
    06 - E
    07 - D
    08 - C
    09 - B
    10 - A
    Após concluir isto você poderia incrementar o programa permitindo que o professor digite o
    gabarito da prova antes dos alunos usarem o programa.
    
    """
    gabarito = []
    respostas_aluno = []
    tira_n = []
    print("\nProfessor: ")
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_certa = gabarito.append(input("Insira a alternativa correta: "))
    n_aluno = 1
    continuar = True
    while continuar != 'n':
        print("\n" * 5)
        print("Aluno n°", n_aluno, ":")
        respostas_aluno.clear()
        for i in range(10):
            print("Questão: ", i + 1)
            resposta_aluno = respostas_aluno.append(input("Escolha a alternativa: "))
        nota = 0
        for i in range(10):
            if respostas_aluno[i] == gabarito[i]:
                nota += 1
        tira_n.append(nota)
        continuar = input("Outro aluno vai utilizar o sistema? RESPONDA COM s OU n : ")
        n_aluno += 1
    print(len(tira_n), "alunos utilizaram o sistema")
    print("\nA maior nota tirada foi: ", max(tira_n))
    print("A menor nota tirada foi: ", min(tira_n))
    print("A media de notas da turma foi de:", sum(tira_n) / len(tira_n))
    print(tira_n)
    
def ex23():
    # exercicio 23
    """Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
    A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
    restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
    sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
    média, conforme a descrição acima informada (retirar o melhor e o pior salto e
    depois calcular a média com as notas restantes). As notas não são informados ordenadas.
    Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    """
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
            
def ex24():
    # exercicio 24
    """Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
    A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos
    restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos
    sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua
    média, conforme a descrição acima informada (retirar o melhor e o pior salto e
    depois calcular a média com as notas restantes). As notas não são informados ordenadas.
    Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
    """
    nome_atleta = True
    n_atleta = 1
    while nome_atleta != '':
        notas = []
        print("\n" * 5)
        print("Atleta", n_atleta)
        nome_atleta = input("Insira o nome do atleta: ")
        if nome_atleta == '':
            break
        else:
            n_jurado = 1
            print("\n" * 3)
            for i in range(7):
                print("Jurado ", n_jurado)
                nota = float(input("Insira a nota: "))
                notas.append(nota)
                n_jurado += 1
            print("Atleta-> ", nome_atleta)
            n_jurado = 1
            count = 0
            for i in range(7):
                print(n_jurado, " Jurado : ", notas[count])
                n_jurado += 1
                count += 1
            print("Resultado Final:")
            print("Nome do atleta: ", nome_atleta)
            print("Melhor nota: ", max(notas))
            print("Pior nota: ", min(notas))
            notas.remove(max(notas))
            notas.remove(min(notas))
            media = sum(notas) / len(notas)
            print("Media: ", round(media, 2))
            n_atleta += 1
            print("\n" * 5)
            


