import numpy as np

##################### VERSÃO 1 (UMA NOVA POPULAÇÃO A CADA ETAPA) ####################

def fitness(individuo):
    n = len(individuo)
    somat1 = (1/n) * np.sum(individuo ** 2)
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))
    result = -20 * np.exp(-0.2 * np.sqrt(somat1)) - np.exp(somat2) + 20 + np.e

    penalidade = 0
    if np.min(individuo) < -32 or np.max(individuo) > 32:
        penalidade = 10_000
    return result + penalidade

def selecao(pop_p):
    pop_i = []

    while len(pop_i) < TAM_POPULACAO:
        p1 = pop_p[np.random.randint(0, TAM_POPULACAO)]
        p2 = pop_p[np.random.randint(0, TAM_POPULACAO)]

        if(fitness(p1) < fitness(p2)): pop_i.append(p1)
        else: pop_i.append(p2)

    return np.array(pop_i)

def crossover(pop_i, tx_crossover=0.7):
    pop_ii = []
    c1 = []
    c2 = []

    while len(pop_ii) < TAM_POPULACAO:
        p1 = pop_i[np.random.randint(low=0, high=TAM_POPULACAO)]
        p2 = pop_i[np.random.randint(low=0, high=TAM_POPULACAO)]

        if np.random.rand() <= tx_crossover:
            half = len(p1) // 2
            
            c1 = np.concatenate([p1[:half], p2[half:]])
            c2 = np.concatenate([p2[:half], p1[half:]])
        else:
            c1, c2 = p1.copy(), p2.copy()

        pop_ii.append(c1)
        pop_ii.append(c2)

    return np.array(pop_ii)

def mutacao(pop_ii, tx_mutacao=0.05):
    pop_iii = []
    
    for individuo in pop_ii:
        indiv_m = individuo.copy()

        if np.random.random() <= tx_mutacao:
            alpha = np.random.normal()
            indiv_m = alpha * individuo

        indiv_m = np.clip(indiv_m, -32, 32)
        pop_iii.append(indiv_m)

    return np.array(pop_iii)

def GA(low, high, dim, geracoes):
    pop_p = np.random.randint(low=low, high=high, size=(TAM_POPULACAO, dim))

    for g in  range(geracoes):
        pop_pi = selecao(pop_p)
        pop_pii = crossover(pop_pi)
        pop_piii = mutacao(pop_pii)

        pop_p = pop_piii
        m = min(pop_p, key=fitness)
        print(fitness(m), g)

    melhor = min(pop_p, key=fitness)
    return fitness(melhor)

TAM_POPULACAO = 100
melhor = GA(-32, 32, 30, 50)
print(melhor)
