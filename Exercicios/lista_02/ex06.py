#Exercicio 06

#Faça um programa que solicite a data de nascimento
dia, mês, ano = input("Insira sua data de nascimento (dd/mm/aaaa):" ).split("/")

meses = ['janeiro',
        'fevereiro',
        'março',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro']
# imprima a data com o nome do mês por extenso
print ('Voce nasceu no dia ->' + ' %s de %s de %s' % (dia, meses[int(mês) - 1], ano))
