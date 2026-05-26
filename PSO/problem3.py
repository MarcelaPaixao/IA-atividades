import numpy as np
import matplotlib.pyplot as plt

def fitness(individuo):
    individuo = np.array(individuo)
    n = len(individuo)
    somat1 = np.sqrt((1/n) * np.sum(individuo ** 2))
    somat2 = (1/n) * np.sum(np.cos(2 * np.pi * individuo))
    return -20 * np.exp(-0.2 * somat1) - np.exp(somat2) + 20 + np.e

#lembrar de usar oclip ou penalidade na fitness
def PSO(low, high, tam_pop, dim, geracoes, w, c1, c2):
    pos = np.random.uniform(low, high, size=(tam_pop, dim))
    vel = np.random.randint(0, size=tam_pop)

    p_best = pos.copy()
    g_best = min(p_best, key=fitness)

    for _ in range(geracoes):
        r1 = np.random.rand()
        r2 = np.random.rand()

        vel = w*vel + c1*r1*(p_best - pos) + c2*r2*(g_best - pos)
        
        pos = np.clip((pos + vel), low, high)

        
        

    
    return fitness(g_best)

w = 0.4
c1 = 2.05
c2 = 2.05

melhor = PSO(-32, 32, 100, 30, 50, w, c1, c2)
print(melhor)