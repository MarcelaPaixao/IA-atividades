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

def selecao(pop):
    pass

def mutacao(pop, tx_m):
    pass

def crossover(pop, tx_cr):
    pass

def GA(tam_pop, dim, geracoes, tx_cr, tx_m):
    pop_p = np.random.randint(low=1, high=5, size=(tam_pop, dim))

    for g in range(geracoes):
        pop_i = selecao(pop_p)
        pop_i = mutacao(pop_i, tx_m)
        pop_i = crossover(pop_i, tx_cr)
        
        pop_p = pop_i.copy()
        print(fitness(min(pop_p, key=fitness)), g)
    

Q = [2.5 * (i+1) for i in range(10)] # em L/s
Comp = [20, 54, 98, 120, 34, 12, 88, 122, 33, 40] # em m

Custo = [65, 98, 150, 210, 340] # em R$/m
D = [150, 200, 250, 300, 400] # em mm

melhor = GA(tam_pop=100, dim=10, geracoes=50, tx_cr=0.7, tx_m=0.1)