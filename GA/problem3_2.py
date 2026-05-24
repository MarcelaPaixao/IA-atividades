import numpy as np

def fitness(individuo):
    n = len(individuo)
    somat1 = np.sqrt((1/n) * np.sum(individuo ** 2))
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))

    result = -20 * np.exp(-0.2 * somat1) - np.exp(somat2) + 20 + np.e

    penalidade = 0
    if min(individuo) < -32 or max(individuo) > 32: penalidade = 10_000

    return result + penalidade

def selecao(i1, i2):
    if(fitness(i1) < fitness(i2)): return i1
    return i2

def crossover(p1, p2, tx_cr=0.7):
    if np.random.rand() <= tx_cr:
        half = len(p1) // 2
        c1 = np.concatenate([p1[:half], p2[half:]])
        c2 = np.concatenate([p2[:half], p1[half:]])
        return c1, c2
    else:
        return p1.copy(), p2.copy()
    
def mutacao(c1, tx_mt=0.1):
    if np.random.rand() <= tx_mt:
        alpha = np.random.normal()
        c1 = c1 * alpha

    c1  = np.clip(c1, -32, 32)
    return c1

def par_aleatorio(pop):
    tam = len(pop)
    return pop[np.random.randint(0, tam)], pop[np.random.randint(0, tam)]

def GA(low, high, geracoes, tam_pop=100, dim=30):
    pop_p = np.random.randint(low=low, high=high, size=(tam_pop, dim))

    for g in range(geracoes):
        pop_i = []
        while len(pop_i) < tam_pop: 
            i1, i2 = par_aleatorio(pop_p)
            melhor = selecao(i1, i2)
            pop_i.append(melhor)
        
        pop_ii = []
        while len(pop_ii) < tam_pop:
            i1, i2 = par_aleatorio(pop_i)
            p1, p2 = crossover(i1, i2)
            pop_ii.append(p1), pop_ii.append(p2)

        pop_iii = []
        for ind in pop_ii:
            i1 = mutacao(ind)
            pop_iii.append(i1)

        pop_p = pop_iii

        m = min(pop_p, key=fitness)
        print(fitness(m), g)
    
    melhor = min(pop_p, key=fitness)
    return fitness(melhor)

melhor = GA(-32, 32, 50)
print(melhor)
