#EXERCICIO 18

def func():
    #tamanho de um arquivo para download (em MB)
    aqrMb=int(input("Insira o tamanho do arquivo MB "))
    #velocidade de um link de Internet (em Mbps)
    veloMBps=int(input("Insira a velocidade de sua Internet "))
    #calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
    #Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos
    resultado = aqrMb / (veloMBps / 8)
    tempo = int( resultado / 60)
    secs = (resultado % 60)
    print("O tempo aproximado de download do arquivo e de aproximadamente", tempo,"minutos e", secs,"segundos")
    print("usando o link de ",veloMBps,"MBps")
    
func()
