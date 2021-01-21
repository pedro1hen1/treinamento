# Exercicio 15

def calctotal():
    valorh = float(input("Insira o valor ganha por hora? " ))
    horasmes = float(input("Insira quantidade de horas trabalha durante o mes "))
    
    #Calcule e mostre o total do seu salário no referido mês
    totalsalariomes = valorh * horasmes
    #11% para o Imposto de Renda
    impostoderenda = totalsalariomes * 0.11
    #8% para o INSS
    inss = totalsalariomes * 0.08
    #5% para o sindicato,
    sindicato = totalsalariomes * 0.05
    #calcule os descontos e o salário líquido
    salarioliq = (totalsalariomes - impostoderenda - inss - sindicato)

    print ('+ Salário Bruto : R$ %.2f' %totalsalariomes)
    print ('- IR: R$ %.2f' %impostoderenda )
    print ('- INSS: R$ %.2f' %inss )
    print ('- Sindicato: R$ %.2f' %sindicato )
    print ('= Salário Liquido : R$ %.2f' %salarioliq)
    
    
calctotal()
