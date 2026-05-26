import numpy as np
import matplotlib.pyplot as plt

def fitness(individuo):
    individuo = np.array(individuo)
    n = len(individuo)
    somat1 = np.sqrt((1/n) * np.sum(individuo ** 2))
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))
    return -20 * np.exp(-0.2 * somat1) - np.exp(somat2) + 20 + np.e

def PSO(low, high, tam_pop, dim, geracoes, w, c1, c2):
    pop = np.random.uniform(low, high, size=(tam_pop, dim))
    vel = np.random.uniform(-1, 1, size=(tam_pop, dim))

    p_best = pop.copy()
    p_best_fitness = [fitness(ind) for ind in pop]
    g_best = min(p_best, key=fitness)
    g_best_fitness = fitness(g_best)
    
    # indice_melhor = np.argmin(p_best_fitness) 
    # g_best = p_best[indice_melhor].copy()
    # g_best_fitness = p_best_fitness[indice_melhor]

    for g in range(geracoes):
        r1 = np.random.rand(tam_pop, dim)
        r2 = np.random.rand(tam_pop, dim)

        vel = w*vel + c1*r1*(p_best - pop) + c2*r2*(g_best - pop)
        pop = np.clip((pop + vel), low, high)

        for p in range(tam_pop):
            particula = pop[p].copy()
            fit_p = fitness(particula)
            if fit_p < p_best_fitness[p]:
                p_best[p] = particula
                p_best_fitness[p] = fit_p
            if fit_p < g_best_fitness:
                g_best = particula
                g_best_fitness = fit_p
           
        print(g_best_fitness, g)
  
    return g_best_fitness

# w = 0.5
# c1 = c2 = 2.05

melhor = PSO(-32, 32, 200, 30, 300, w=0.5, c1=2.05, c2=2.05)
print(melhor)