import random
import math

def funcao_retorno(sol):
    x1, x2, x3, x4 = sol
    
    a = 50 * x1 - 1.2 * x1 ** 2
    b = 45 * x2 - 1.0 * x2 ** 2 
    c = 40 * x3 - 0.8 * x3 ** 2
    d = 55 * x4 - 1.5 * x4 ** 2
    
    return a + b + c + d

def verifica_restricoes(sol):
    """
    Restrições:
    1. Soma total <= 50
    2. LinkedIn Ads + YouTube Ads  <= 25
    3. Horas <= 80
    """
    
    x1, x2, x3, x4 = sol

    if min(sol) < 0:
        return False
    
    horas_total = 2*x1 + x2 + 3*x3 + 2*x4
    return horas_total <= 80 and sum(sol) <= 50 and (x3 + x4 <= 25)

def gerar_vizinhos(sol):
    vizinhos = []

    for i in range(4):
        for delta in [-1, 1]:
            nova = list(sol)
            nova[i] += delta

            if verifica_restricoes(nova):
                vizinhos.append(tuple(nova))
        
    return vizinhos

def hill_climbing(sol):
    # atual = (0, 0, 0, 0)
    atual = sol

    while True:
        vizinhos = gerar_vizinhos(atual)

        if not vizinhos:
            break

        melhor = max(vizinhos, key=funcao_retorno)

        if funcao_retorno(melhor) <= funcao_retorno(atual):
            break

        atual = melhor

    return atual

def vizinho_aleatorio(sol):
    while True:
        nova = list(sol)

        i = random.randint(0, 3)
        delta = random.choice([-1, 1])

        nova[i] += delta

        if verifica_restricoes(nova):
            return tuple(nova)
        
def simulated_annealing():
    atual = (0, 0, 0, 0)
    melhor = atual

    T = 98.0 # Temperatura inicial
    T_min = 0.05 # Temperatura mínima
    alpha = 0.99 # Taxa de resfriamento (cooling rate)

    while T > T_min:
        candidato = vizinho_aleatorio(atual)

        delta = funcao_retorno(candidato) - funcao_retorno(atual)

        if delta > 0:
            atual = candidato
        else:
            prob = math.exp(delta / T)

            if random.random() < prob:
                atual = candidato

        if funcao_retorno(atual) > funcao_retorno(melhor):
            melhor = atual

        T *= alpha

    return melhor


if __name__ == "__main__":
    
    solucao1 = simulated_annealing()
    solucao = hill_climbing(solucao1)

    print("Melhor plano de produção encontrado:")
    print(f"Google Ads: {solucao[0]*1000}")
    print(f"Instagram Ads: {solucao[1]*1000}")
    print(f"LinkedIn Ads: {solucao[2]*1000}")
    print(f"YouTube Ads: {solucao[3]*1000}")
    print(f"Lucro Máximo: R$ {funcao_retorno(solucao)*1000}")
