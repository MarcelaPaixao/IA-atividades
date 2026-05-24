import numpy as np

def fitness(individuo):
    individuo = np.array(individuo)
    n = len(individuo)
    somat1 = np.sqrt((1/n) * np.sum(individuo ** 2))
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))
    return -20 * np.exp(-0.2 * somat1) - np.exp(somat2) + 20 + np.e

def mutacao(pop, F, low, high):
    i1, i2, i3 = np.random.choice(len(pop), size=3, replace=False)
    vi = pop[i1] + F * (pop[i2] - pop[i3])
    return np.clip(vi, low, high)

def crossover(pop_orig, pop_mut, Cr):
    i_o = pop_orig[np.random.randint(0, len(pop_orig))]
    i_m = pop_mut[np.random.randint(0, len(pop_mut))]

    i_c = []
    for gene in range(len(i_o)):
        if np.random.rand() <= Cr: i_c.append(i_o[gene])
        else: i_c.append(i_m[gene])

    return i_c

def selecao(pop):
    i1, i2 = np.random.choice(len(pop), size=2, replace=False)
    if fitness(pop[i1]) < fitness(pop[i2]): return pop[i1]
    else: return pop[i2]

# N deve ser maior ou igual a quatro para garantir o funcionamento do algoritmo!
def DE(low, high, N, D, G, F, Cr):
    pop_p = np.random.randint(low=low, high=high, size=(N, D))
    
    for g in range(G):
        pop_i = []
        while len(pop_i) < N: pop_i.append(mutacao(np.array(pop_p), F, low, high))
        
        pop_ii = []
        while len(pop_ii) < N: pop_ii.append(crossover(pop_p, pop_i, Cr))

        pop_iii = []
        while len(pop_iii) < N: pop_iii.append(selecao(pop_ii))

        pop_p = pop_iii
        print(fitness(min(pop_p, key=fitness)), g)
    
    melhor = min(pop_p, key=fitness)
    return fitness(melhor)


print(DE(low=-32, high=32, N=100, D=30, G=50, F=0.4, Cr=0.8))