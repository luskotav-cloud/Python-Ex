import random
mss = []

def simularPing(endereco = str(input("Digite o endereço: ")), tentativas=5):

    for c in range(5):
        ms = random.randint(10, 300)
        mss.append(ms)
        
    
    print(f"O endereço mais lento foi: {max(mss)}\nO endereço mais veloz foi: {min(mss)}")
    print(f"Todos os ms: {mss}")

simularPing()
