import random

def simular_pacotes_dos():
    ip_atacar = str(input("Qual ip você deseja atacar? "))

    print(f"O ip: {ip_atacar}, recebeu: {random.randint(1000, 50000)} pacotes")

simular_pacotes_dos()
