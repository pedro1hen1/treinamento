#E05: IMC
"""---- para executar def calcIMC():------
O IMC (Índice de Massa Corporal) é um índice utilizado para detectar casos de obesidade ou desnutrição, principalmente em estudos que envolvem grandes populações. Para a avaliação de um paciente individualmente, no entanto, ele pode ser falho por não levar em conta a composição desse peso corporal, que pode ser composto por gordura, músculos, água e estruturas ósseas.

O IMC é calculado dividindo o peso pela altura elevada ao quadrado. 

Tabela de resultados - IMC

O IMC pode trazer os seguintes resultados:

IMC 	Resultado
Menos do que 18,5 	Abaixo do peso
Entre 18,5 e 24,9 	Peso normal
Entre 25 e 29,9 	Sobrepeso
Entre 30 e 34,9 	Obesidade grau 1
Entre 35 e 39,9 	Obesidade grau 2
Mais do que 40 	Obesidade grau 3

Poste a url do projeto com a resposta"""

def calcIMC():
    print("\nIMC 	Resultado:\n" + 
          "Menos do que 18,5 	Abaixo do peso\n" +
          "Entre 18,5 e 24,9 	Peso normal\n" +
          "Entre 25 e 29,9 	Sobrepeso\n" +
          "Entre 30 e 34,9 	Obesidade grau 1\n"+
          "Entre 35 e 39,9 	Obesidade grau 2\n" +
          "Mais do que 40 	        Obesidade grau 3\n ")
    # entrada
    peso = float(input('Insira seu peso? '))
    altura = float(input('Insira sua altura? '))
    
    imc = peso /(altura**2)
    if imc < 18.5:
      cond = 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
      cond= 'Peso Normal.'
    elif 25 <= imc < 29.9:
      cond ='Sobrepeso'
    elif 30 <= imc < 34.9:
      cond ='Obesidade grau 1'
    elif 35 <= imc < 39.39:
      cond = 'Obesidade grau 2'
    else:
      cond ='Obesidade grau 3'
    
    #impressão
    print("Seu peso =>", peso)
    print("Sua altura =>", altura)
    print('IMC ->', imc)
    print('Sua classificação é ->', cond)
    
calcIMC()