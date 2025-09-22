logs_servidor = [23, 45, 15, 88, 120, 30, 42, 12, 95]

def analisar_latencia():
    print(min(logs_servidor), "Milissegundos de resposta minimo")
    print(max(logs_servidor), "Milissegundos de resposta máxima")

analisar_latencia()
