import numpy as np

TAM_POPULACAO = 100

def fitness(individuo):
    n = 30
    somat1 = 1/n * np.sum(individuo ** 2)
    somat2 = 1/n * np.sum(np.cos(2 * np.pi * individuo))
    result = -20 ** np.exp(-0.2 * np.sqrt(somat1)) - np.exp(somat2) + 20 + np.e

    penalidade = 0
    if result < -32 or result > 32: penalidade = 10000
    
    return result + penalidade

def selecao(pop_p):
    p1 = np.random.choice(pop_p)
    p2 = np.random.choice(pop_p)
    pop_i = []

    for _ in range(TAM_POPULACAO):
    # while len(pop_i) < TAM_POPULACAO:
        if(fitness(p1) < fitness(p2)): pop_i.append(p1)
        else: pop_i.append(p2)

    return np.array(pop_i)

def crossover(pop_i, tx_crossover=0.7):
    pop_ii = []
    c1 = []
    c2 = []

    for _ in range(TAM_POPULACAO/2):
    # while len(pop_ii) < TAM_POPULACAO:]
        p1 = np.random.choice(pop_i)
        p2 = np.random.choice(pop_i)
        beta = np.random.normal(0, 1)

        if beta >= tx_crossover:
            half = len(p1)/2
            c1 = p1[half:] + p2[:half]
            c2 = p2[half:] + p1[:half]

        else:
            c1  = p1
            c2 = p2

        pop_ii.append(c1)
        pop_ii.append(c2)

    return np.array(pop_ii)

def mutacao(pop_ii, tx_mutacao=0.1):
    pop_iii = []
    

    for individuo in pop_ii:
        alpha = np.random.normal(0, 1)
        
        indiv_m = np.zeros(len(individuo))
        if alpha >= tx_mutacao:
            indiv_m = alpha * individuo
        else:
            indiv_m = individuo
        
        pop_iii.append(indiv_m)

    return np.array(pop_iii)

