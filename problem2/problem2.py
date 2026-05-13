import random
import numpy as np

def funcao_objetivo(sol):
    x = sol # não precisa disso, coloque apenas para manter a clareza de quem é 'sol'
    return x * np.sin(10 * np.pi * x) + 1


def verifica_restricoes(sol):
    return sol >= -1 and sol <= 2

def gerar_vizinhos(sol):
    vizinhos = []

    for delta in [-0.7, 0.7]:
        nova = sol + delta
        if verifica_restricoes(nova):
            vizinhos.append(nova)
    
    return vizinhos

def hill_climbing(sol):
    atual = sol

    while True:
        vizinhos = gerar_vizinhos(atual)

        if not vizinhos:
            break

        melhor = max(vizinhos, key=funcao_objetivo)

        if(funcao_objetivo(melhor) <= funcao_objetivo(atual)):
            break

        atual = melhor

    return atual

def gerar_vizinhos_aleatorios(sol):
    pass

def simulated_annealing():
    pass

if __name__ == "__main__":
    # solucao1 = simulated_annealing()
    solucao = hill_climbing(1)

    print("Melhor solução encontrada:")
    print(f"X: {solucao}")

#Preciso plotar o grafico para visualizar direito o que tá acontecendo!!