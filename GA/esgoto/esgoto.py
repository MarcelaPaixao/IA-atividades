import numpy as np

def fitness(individuo):
    penalidade = 0
    custo = 0

    for i in range(len(individuo)):        
        d = D[individuo[i]]/1000
        custo += Custo[individuo[i]] * Comp[i]
        q = Q[i]/1000

        A = (np.pi * d ** 2)/4
        Rh = d/4

        q_max = (A * Rh ** (2/3) * np.sqrt(0.005))/0.0013
        
        if  q > 0.75 * q_max:
            penalidade += 10_000
    
    return custo + penalidade

def selecao(pop, tam_pop):
    pop_i = []
    
    while len(pop_i) < tam_pop:
        i1 = pop[np.random.randint(0, tam_pop)]
        i2 = pop[np.random.randint(0, tam_pop)]
        
        if fitness(i1) < fitness(i2): pop_i.append(i1)
        else: pop_i.append(i2)

    return np.array(pop_i)

def crossover(pop, tx_cr, tam_pop):
    pop_i = []
    while  len(pop_i) < tam_pop:
        p1 = pop[np.random.randint(0, tam_pop)]
        p2 = pop[np.random.randint(0, tam_pop)]
        
        if np.random.rand() <= tx_cr:
            idx = np.random.randint(0, len(p1))
            pop_i.append(np.concatenate([p1[:idx], p2[idx:]]))
            pop_i.append(np.concatenate([p2[:idx], p1[idx:]]))

        else: 
            pop_i.append(p1)
            pop_i.append(p2)

    return np.array(pop_i)

def mutacao(pop, tx_m):
    pop_i = []
    for ind in pop:
        ind_m = ind.copy()
        for i in range(len(ind_m)):
            if np.random.rand() <= tx_m:
                ind_m[i] = np.random.randint(0, 5)
        
        pop_i.append(ind_m)

    return np.array(pop_i)


def GA(tam_pop, dim, geracoes, tx_cr, tx_m):
    pop_p = np.random.randint(low=0, high=5, size=(tam_pop, dim))

    for g in range(geracoes):
        selecionados = selecao(pop_p, tam_pop)
        cruzados = crossover(selecionados, tx_cr, tam_pop)
        mutados = mutacao(cruzados, tx_m)
        
        pop_p = mutados
        
        # m = min(pop_p, key=fitness)
        # print(fitness(m), g)      

    melhor = min(pop_p, key=fitness)
    return fitness(melhor)
    

Q = [2.5 * (i+1) for i in range(10)] # em L/s
Comp = [20, 54, 98, 120, 34, 12, 88, 122, 33, 40] # em m

Custo = [65, 98, 150, 210, 340] # em R$/m
D = [150, 200, 250, 300, 400] # em mm

melhor = GA(tam_pop=100, dim=10, geracoes=50, tx_cr=0.7, tx_m=0.1)
print(melhor)